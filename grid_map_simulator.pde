int w = 10, h = 10, bs = 60;
/*
w = number of columns
h = number of rows
bs = pixels per box
*/
float obs = bs * 0.8; //obstacle size

float wp = bs * 0.8; //waypoint size

float mp = (bs - obs)/2; //midpoint of grid to draw object

int[][] board = new int[h][w];

int[] segments = new int[8];
int v = 0; //coordniates counter
int segAid = 0; //segment area index

ArrayList<int[]> segmentList; //dynamic array

Boolean segmentMode = false;

void setup(){
  size(600, 600); //change according to (w*bs) and (h*bs)
  ellipseMode(CORNER);
  segmentList = new ArrayList<int[]>();
}

void draw(){
  for(int j=0; j<h; j++){
    for(int i=0; i<w; i++){
      fill(255);
      stroke(0);
      rect(i*bs, j*bs, bs, bs);
      if(board[j][i] == -1){ //sets obstacles in black squares
        fill(0, 0, 0);
        noStroke();
        rect(((i*bs)+mp), ((j*bs)+mp), obs, obs);      
      }
      else
        if(board[j][i] == 1){ //sets navigation points in green circle with blue background
          fill(186, 186, 186);
          rect(i*bs, j*bs, bs, bs);    
          fill(0, 255, 0);
          noStroke();
          ellipse(((i*bs)+mp), ((j*bs)+mp), wp, wp);
        }
        else
          if(board[j][i] == 2){ //sets navigation points in red circle with blue background
            fill(186, 186, 186);
            rect(i*bs, j*bs, bs, bs);    
            fill(255, 0, 0);
            noStroke();
            ellipse(((i*bs)+mp), ((j*bs)+mp), wp, wp);
          }
          else
            if(board[j][i] == 3){ //sets segmenteed areas in blue squares
              fill(186, 186, 186);
              rect(i*bs, j*bs, bs, bs);      
            }
    }  
  }
}

void mouseDragged(){
  board[mouseY/bs][mouseX/bs] = -1; 
}

void mousePressed(){
  board[mouseY/bs][mouseX/bs] = board[mouseY/bs][mouseX/bs] * -1;
  
  //feature#1-segmentation
  if(segmentMode == true){
    segments[v*2] = (mouseX/bs);
    segments[(v*2)+1] = (mouseY/bs);
    v++;
    if(v == 4){
      segmentArea(segments);
      segmentList.add(new int[]{segments[0], segments[1], segments[2], segments[3], segments[4], segments[5], segments[6], segments[7]});
      segmentMode = false;
      v = 0;
    }
  }
}

void keyPressed(){
  if((key == 'S') || (key == 's')){ //set start point by moving the cursor onto the grid and press 's'
    board[mouseY/bs][mouseX/bs] = 1;
  }
  if((key == 'E') || (key == 'e')){ //set end point by moving the cursor onto the grid and press 'e'
    board[mouseY/bs][mouseX/bs] = 2;
  }
  if((key == 'I') || (key == 'i')){ //export the grid map as an image 
    save("map.jpg");
  }
  if((key == 'D') || (key == 'd')){ 
    segmentMode = true;
  }
  if((key == 'L') || (key == 'l')){ //export segment dimensions and waypoints
    for(int[] xy : segmentList){
        
        //segment dimensions
        int colSize = ((xy[0] - xy[6]) + 1);
        int roSize = ((xy[5] - xy[7]) + 1);
        
        //start and end points
        int vertCount = 0; //counter for verticeID
        int sp = -1, ep = -1;
        
        int colStart = xy[6], colEnd = xy[0];
        int roStart = xy[7], roEnd = xy[5];
        
        for(int cs = colStart; cs <= colEnd; cs++){
          for(int rs = roStart; rs <= roEnd; rs++){
            if(board[rs][cs] == 1){
              sp = vertCount;
            }
            if(board[rs][cs] == 2){
              ep = vertCount;
            }
            vertCount++;
          }
        }
        
        //export to text file
        String list[] = new String[2];
        list[0] = str(colSize) + "x" + str(roSize);
        list[1] = str(sp) + ">>" + str(ep);
        saveStrings("segment-" + str(segAid++) + ".txt", list);
    }
  }
}

//set the grids of segmented areas with a value of 3
void segmentArea(int[] s){
  int colStart = s[6], colEnd = s[0];
  int roStart = s[7], roEnd = s[5];
  
  for(int cs = colStart; cs <= colEnd; cs++){
    for(int rs = roStart; rs <= roEnd; rs++){
      board[rs][cs] = 3;
    }
  }
}