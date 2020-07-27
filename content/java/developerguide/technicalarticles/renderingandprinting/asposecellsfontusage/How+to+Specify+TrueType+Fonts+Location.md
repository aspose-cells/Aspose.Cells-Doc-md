+++
title = "How to Specify TrueType Fonts Location" 
description = "" 
weight = 20372 
+++

Aspose.Cells for Java : How to Specify TrueType Fonts Location  

# Aspose.Cells for Java : How to Specify TrueType Fonts Location


This article describes:

1.  [Where the Aspose.Cells API looks for TrueType fonts](https://docs2.aspose.com/cells/java/developerguide/technicalarticles/renderingandprinting/asposecellsfontusage/how+to+specify+truetype+fonts+location).
2.  [How to explicitly specify a TrueType font folders for Aspose.Cells API](https://docs2.aspose.com/cells/java/developerguide/technicalarticles/renderingandprinting/asposecellsfontusage/how+to+specify+truetype+fonts+location).
3.  [How to restrict the Aspose.Cells API to use only one TrueType fonts location](https://docs2.aspose.com/cells/java/developerguide/technicalarticles/renderingandprinting/asposecellsfontusage/how+to+specify+truetype+fonts+location).

### Working with Fonts

#### Where Aspose.Cells Looks for TrueType Fonts on Windows

Aspose.Cells searches for fonts in the **Windows\\Fonts** folder. This default setting works most of the time so only specify your own fonts folders if you really need to.

#### Where Aspose.Cells Looks for TrueType Fonts on Linux

By default, Aspose.Cells API looks for the fonts in all of the the following locations, although different Linux distributions store fonts in different folders.

1.  /usr/share/fonts
2.  /usr/local/share/fonts

This default behavior will work for most Linux distributions, but is not guaranteed to work all of the time. You might need to specify the location of the TrueType fonts explicitly.

#### How to Explicitly Specify a Font Folder

Aspose.Cells APIs have exposed many factory methods for the `FontConfigs` class to specify the fonts or fonts folders as described below.

1.  The `setFontFolder` method accepts first parameter of type `String` with location to the fonts directory whereas the second parameter of type `Boolean` is to direct the Aspose.Cells APis to search the folders recursively for font files.
2.  The `setFontFolders` method accepts an array of type `String` so you may specify many font directories using this approach. You may also direct the Aspose.Cells APis to search the folders recursively by specifying `true` as second parameter.
3.  The `setFontSources` method accepts an array of type `FontSourceBase` for you to specify a list of individual fonts' locations.

When specifying the fonts folder using any of the above mentioned methods, we recommend setting the font location at the start of the application otherwise you may receive poorly formatted results.

Setting the fonts folder using any of the above methods does not ensure that the Aspose.Cells API will not look for the fonts on default locations such as system's font folder.

#### How to Restrict the Aspose.Cells to Use Only One Font Folder

Starting from Aspose.Cells for Java 8.1.0, setting the JVM arguments as **\-DAspose.Cells.FontDirExc="YourFontDir** will ensure that the Aspose.Cells API will only use the fonts location as specified.

Set the specified arguments using the `System.setProperty` method as shown below.

{{< code lang="cs" >}}
System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");
{{< /code >}}

Please note the following:

*   The above statement should be at the start of your application.
*   Using the above approach does not require setting the font directory using any of the `FontConfigs` methods discussed above.
*   The string "FontDirSet" should be the complete path to the folder containing the required fonts.

