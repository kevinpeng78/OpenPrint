import java.awt.Frame;
import java.awt.*;

//add extrusion factor

public class gui extends Frame{
    private Label printSpeed;
    private Label nLines;
    private Label lineLength;
    private Label layerSeparation;
    private Label bedX;
    private Label bedY;
    private TextField printSpeedField;
    private TextField nLinesField;
    private TextField lineLengthField;
    private TextField layerSeparationField;
    private TextField bedXField;
    private TextField bedYField;
    public static final int LEFT = Label.LEFT;    // Label.LEFT
    public static final int RIGHT = Label.RIGHT;   // Label.RIGHT
    public static final int CENTER = Label.CENTER;  // Label.CENTER

    public gui(){
        setLayout(new FlowLayout());
        printSpeed = new Label("Enter print speed", LEFT);
        add(printSpeed);
        printSpeedField = new TextField("", 10);
        add(printSpeedField);
        nLines = new Label("Enter nLines", LEFT);
        add(nLines);
        nLinesField = new TextField("", 10);
        add(nLinesField);
        lineLength = new Label("Enter nLines", CENTER);
        add(lineLength);
        lineLengthField = new TextField("", 10);
        add(lineLengthField);
        layerSeparation = new Label("Enter layerSeparation", RIGHT);
        add(layerSeparation);
        layerSeparationField = new TextField("", 10);
        add(layerSeparationField);
        bedX = new Label("Enter bed X dimensions", RIGHT);
        add(bedX);
        bedXField = new TextField("", 10);
        add(bedXField);
        bedY = new Label("Enter bed Y dimensions", RIGHT);
        add(bedY);
        bedYField = new TextField("", 10);
        add(bedYField);
        
        setTitle("gui");
        setSize(300, 100);
        setVisible(true);
        

    }
    public static void main(String[] args){
        new gui();
    }
}