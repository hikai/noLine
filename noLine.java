package noLine;

import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

public class noLine {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BufferedImage tgImg = null;
		try {
			tgImg = ImageIO.read(new File("target.png"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		tgImg = lineDelet(tgImg, 254,3);
		
		
		try {
			ImageIO.write(tgImg, "png", new File("out.png"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
	
	public static BufferedImage lineDelet(BufferedImage input, int knee,int count){
		BufferedImage output = input;
		
		float[] mask = {
				(float) 1,
				(float)-1};
		
		
		for (int x = 0; x < input.getWidth(); x++) {
			for (int y = 0; y < input.getHeight(); y++) {
				
				
				
				int Edge = 0;
				for(int i = 0; i < mask.length;i++){
					try{
						Color color = new Color(input.getRGB(x, y+i));
						System.out.print(color.getRed()+ " ");
						
						//������ ��� �̹����̴� rgb�뷱���� ���� ������ ���� r�������� �����
						Edge += color.getRed() * mask[i];
					}
					catch(IndexOutOfBoundsException e){
						
					}
				}
				
				//System.out.println(Edge);
				Edge = Math.abs(Edge);
				System.out.println(" = "+Edge);
				
				
				if(Edge > knee){
					output.setRGB(x, y, (new Color(Edge, Edge, Edge).getRGB()));
				}else{
					
				}
				
			}
		}
		
		
		return count==0?output:lineDelet(input, knee, count-1);
	}

}
