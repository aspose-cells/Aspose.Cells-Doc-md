##Setup and Installation Guidelines
"setup Aspose.Cells for PHP via Java and installation guidelines."
## **System Requirements**
Aspose.Cells for PHP via Java is platform independent API and can be used on any platform (Windows, Linux, MacOS etc.) where [PHP](https://www.php.net/downloads.php) 7 or greater versions is installed. The machine must have Oracle JDK 7 or greater versions before setting up the installation.
## **Installation and Usage**
Aspose.Cells for PHP via Java is distributed as a ZIP archive.
To setup environment, install and use Aspose.Cells for PHP via Java, follow the instructions:
### **Linux:**
- Download [PHP](https://www.php.net/downloads.php) source and  install it. Or, use “sudo apt install php-xxx” command to install php binary.
- Install Oracle JDK (1.7 or 1.8) for Linux, configure JAVA_HOME environment variable.
- Download/Get "Aspose.Cells for PHP via Java" API and extract it. There will be a folder named "aspose.cells".
- Download PHP/Java Bridge binary (JavaBridge.jar) from http://php-java-bridge.sourceforge.net/pjb/download.php and save it into "aspose.cells" folder.
- Download java/Java.inc PHP library (Java.inc) from http://php-java-bridge.sourceforge.net/pjb/download.php and save it into "aspose.cells" folder.
- Run “PHP/Java Bridge” in the above folder with below command.
|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCAL:8080 >/dev/null 2>&1 &|
| :- |
- Run "example.php" in “aspose.cells” folder to run the example with below command:
|$ php example.php|
| :- |
### **Windows:**
- Download [PHP](https://www.php.net/downloads.php) windows binary and add "php.exe" to PATH.
- Install Oracle JDK (1.7 or 1.8) for Windows and configure JAVA_HOME environment variable.
- Download "Aspose.Cells for PHP via Java" API and extract it. There will be a folder named "aspose.cells".
- Download PHP/Java Bridge binary (JavaBridge.jar) from http://php-java-bridge.sourceforge.net/pjb/download.php and save it into "aspose.cells" folder.
- Download java/Java.inc PHP library (Java.inc) from http://php-java-bridge.sourceforge.net/pjb/download.php and save it into "aspose.cells" folder.
- Run “PHP/Java Bridge” in the above folder with below command. Select 8080 http listener port when the bridge started and click OK button.
|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- Run "example.php" in “aspose.cells” folder to run the example with below command:
|> php example.php|
| :- |
### **Mac:**
- Install [PHP](https://www.php.net/downloads.php).
- Install Oracle JDK (1.7 or 1.8) for Mac, configure JAVA_HOME environment variable.
- Download "Aspose.Cells for PHP via Java" API and extract it. There will be a folder named "aspose.cells".
- Download PHP/Java Bridge binary (JavaBridge.jar) from http://php-java-bridge.sourceforge.net/pjb/download.php and save it into "aspose.cells" folder.
- Download java/Java.inc PHP library (Java.inc) from http://php-java-bridge.sourceforge.net/pjb/download.php and save it into "aspose.cells" folder.
- Run “PHP/Java Bridge” in the above folder with below command. Select 8080 http listener port when the bridge started and click OK button.
|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- Run "example.php" in “aspose.cells” folder to run the example with below command:
|$ php example.php|
| :- |
