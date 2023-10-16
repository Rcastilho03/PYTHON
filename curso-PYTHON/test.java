import java.util.HashMap;

public final class test {

  static HashMap<String,Integer> seqStateMachine = new HashMap<String,Integer>();
  static int homePosition = 0;
  static int x = 3;
  static int y = 9;
  public static void main(String... args) {
  
        seqStateMachine.put("HighCone", 0);
        seqStateMachine.put("MidCone",0);
        seqStateMachine.put("LowCone",0);

        seqStateMachine.put("HighCube", 0);
        seqStateMachine.put("MidCube",0);
        seqStateMachine.put("LowCube",0);

        seqStateMachine.put("SingleSubstation", 0);
        seqStateMachine.put("DoubleSubstation",0);
        seqStateMachine.put("Home",0);

        System.out.println(seqStateMachine);
        setSeqStateMachine("Home",1);
        homePosition = getSeqStateMachine("Home");
        System.out.println(seqStateMachine);
        System.out.println(homePosition);


        if (homePosition == 1){
          System.out.println(x*y);
        }
        else{
          System.out.println(y-x);
        }



        resetStateMachine();
        System.out.println(seqStateMachine);
        
        if (homePosition == 1){
          System.out.println(x*y);
        }
        else{
          System.out.println(y-x);
        }

  }

  public static void setSeqStateMachine(String key,int value) {
        seqStateMachine.replace(key, value);
    }

  public static int getSeqStateMachine(String key) {
      return seqStateMachine.get(key);
  }

    public static void resetStateMachine(){
        seqStateMachine.replace("HighCone", 0);
        seqStateMachine.replace("MidCone",0);
        seqStateMachine.replace("LowCone",0);

        seqStateMachine.replace("HighCube", 0);
        seqStateMachine.replace("MidCube",0);
        seqStateMachine.replace("LowCube",0);

        seqStateMachine.replace("SingleSubstation", 0);
        seqStateMachine.replace("DoubleSubstation",0);
        seqStateMachine.replace("Home",0);
    }
}