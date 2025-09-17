##How to fix java.lang.ClassNotFoundException
Learn How to fix java.lang.ClassNotFoundException in the Aspose.Cells for Java.
Aspose.Cells for Java API depends on some additional libraries, if they are missing, an exception may be thrown as "java.lang.ClassNotFoundException".
This article lists such kind of exceptions and explains which libraries are installed to resolve them.
## How to fix ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
### **Summary**
Aspose.Cells for Java API depends on Bouncy Castle for encryption and decryption features, that is, if the program is required to load or save encrypted spreadsheets, it is required to add reference of bcprov-jdk16-146.jar in the project's class path.
### **Symptoms**
You may get the java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider.
### **Solution**
The solution is actually very simple as detailed below.
1. Download any major release of [Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Extract the downloaded archive and browse to \JDK 1.6\aspose-cells-x.x.0-java\lib directory.
1. Reference the bcprov-jdk16-146.jar in the class path of the project.
Alternatively, you can add the dependency in the pom.xml and let the project resolve the dependency via maven.
