package week10.decorator;
public class MockedDocument implements Document{
    public String gcsPath;
    @Override
    public String parse(){
        try {
            Thread.sleep(200);
        } catch (InterruptedException e) {
            
            e.printStackTrace();
        }
        return "Mocked paerce";
    }

    @Override
    public String getGcsPath() {
        return gcsPath;
    }
}
