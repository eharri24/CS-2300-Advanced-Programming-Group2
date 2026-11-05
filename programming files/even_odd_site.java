

import java.io.*;
// This class creates a table in html that seperates numbers 1 through 50 into even and odd columns
public class even_odd_site {
    public static void main(String[] args) throws IOException {
        // opening a BufferedWriter to overwrite numbers.html
        BufferedWriter file = new BufferedWriter(new FileWriter("numbers.html"));
        file.write("<html>\n<head>\n<title>List of Numbers</title>\n</head>\n<body>\n");
        file.write("<table>\n<tr><th>Even Numbers</th><th>Odd Numbers</th></tr>\n");
        // looping through 1-50
        for (int i = 1; i <= 50; i++) {
            //if the number is even, the number is placed in first column
            if (i % 2 == 0) {
                file.write("<tr><td>" + i + "</td><td></td></tr>\n");
            }
            //if the number is odd, the number is placed in the next columns
            else {
                file.write("<tr><td></td><td>" + i + "</td></tr>\n");
            }
        }
        file.write("</table>\n</body>\n</html>");
        file.close();
        BufferedReader reader = new BufferedReader(new FileReader("numbers.html"));
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
        reader.close();
    }
}
