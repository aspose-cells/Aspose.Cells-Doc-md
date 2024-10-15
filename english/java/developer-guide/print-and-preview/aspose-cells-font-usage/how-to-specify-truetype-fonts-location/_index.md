---
title: How to Specify TrueType Fonts Location
type: docs
weight: 30
url: /java/how-to-specify-truetype-fonts-location/
---

{{% alert color="primary" %}}

This article describes:

1. [Where the Aspose.Cells API looks for TrueType fonts](/cells/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows).
1. [How to explicitly specify a TrueType font folders for Aspose.Cells API](/cells/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder).
1. [How to restrict the Aspose.Cells API to use only one TrueType fonts location](/cells/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder).

{{% /alert %}}

## **Working with Fonts**

### **Where Aspose.Cells Looks for TrueType Fonts on Windows**

Aspose.Cells searches for fonts in the **Windows\Fonts** folder. This default setting works most of the time so only specify your own fonts folders if you really need to.

### **Where Aspose.Cells Looks for TrueType Fonts on Linux**

By default, Aspose.Cells API looks for the fonts in all of the the following locations, although different Linux distributions store fonts in different folders.

1. /usr/share/fonts
1. /usr/local/share/fonts

{{% alert color="primary" %}}

This default behavior will work for most Linux distributions, but is not guaranteed to work all of the time. You might need to specify the location of the TrueType fonts explicitly. 

{{% /alert %}}

### **How to Explicitly Specify a Font Folder**

Aspose.Cells APIs have exposed many factory methods for the FontConfigs class to specify the fonts or fonts folders as described below.

1. The setFontFolder method accepts first parameter of type String with location to the fonts directory whereas the second parameter of type Boolean is to direct the Aspose.Cells APis to search the folders recursively for font files.
1. The setFontFolders method accepts an array of type String so you may specify many font directories using this approach. You may also direct the Aspose.Cells APis to search the folders recursively by specifying true as second parameter.
1. The setFontSources method accepts an array of type FontSourceBase for you to specify a list of individual fonts' locations.

{{% alert color="primary" %}}

When specifying the fonts folder using any of the above mentioned methods, we recommend setting the font location at the start of the application otherwise you may receive poorly formatted results.

{{% /alert %}} {{% alert color="primary" %}}

Setting the fonts folder using any of the above methods does not ensure that the Aspose.Cells API will not look for the fonts on default locations such as system's font folder.

{{% /alert %}}

### **How to Restrict the Aspose.Cells to Use Only One Font Folder**

Starting from Aspose.Cells for Java 8.1.0, setting the JVM arguments as **-DAspose.Cells.FontDirExc="YourFontDir** will ensure that the Aspose.Cells API will only use the fonts location as specified.

Set the specified arguments using the System.setProperty method as shown below.

{{< highlight java >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

Please note the following:

- The above statement should be at the start of your application.
- Using the above approach does not require setting the font directory using any of the FontConfigs methods discussed above.
- The string "FontDirSet" should be the complete path to the folder containing the required fonts.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}