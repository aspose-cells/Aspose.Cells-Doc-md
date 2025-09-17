##Installation
## **Installing Aspose.Cells for Java from Maven Repository**
Aspose hosts all Java APIs on [Maven repository](https://releases.aspose.com/java/repo/). You can easily use [Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) directly in your Maven Projects with simple configurations.
First, you need to specify Aspose Maven Repository configuration/location in your Maven pom.xml as below:
for Gradle in you build.gradle script as follows:
//Add Aspose maven repository
repositories {
mavenCentral()
maven {
url "https://releases.aspose.com/java/repo/"
}
}
Then define Aspose.Cells for Java API dependency in your pom.xml as follows (This will include everything, e.g main jar file, Java Docs, and other libraries accordingly):
Congratulations! You have successfully defined the Aspose.Cells for Java Maven dependency in your Maven project.
## **WebP Image Loading**
WebP is a modern image format. It is designed to produce smaller file sizes, while maintaining high visual quality.
Currenlty, In Microsoft Excel, WebP images are not allowed to be inserted directly. However,  there are cases that WebP images are inserted into Excel source files directly by some third party libraries.
Generally Aspose.Cells for Java uses Java's ImageIO to load raster images, currently the JDK itself doesn't support to load WebP images. Some additional plugins or extensions(e.g. [imageio-webp Plugin](https://mvnrepository.com/artifact/com.twelvemonkeys.imageio/imageio-webp)) is needed for Java's ImageIO to load WebP images.
## **Support**
Please check the following to get quick technical support
[Aspose.Cells - Forums](https://forum.aspose.com/c/cells/9)
