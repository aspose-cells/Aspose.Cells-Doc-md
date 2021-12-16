---
title: Excel Themes and Colors
type: docs
weight: 100
url: /net/excel-themes-and-colors/
---

## **Excel Themes and Colors**

Themes provide a unified look with named styles, graphical effects and other objects used in a workbook. For example, the Accent1 style, for example, looks different in the Office and the Apex themes. Often, you apply a document theme and then amend it to how you want it.

Aspose.Cells provides features for customizing themes and colors.

### **Get and Set Theme Colors**

Below are a few methods and properties that implement theme colors.

- [**Style.ForegroundThemeColor**](https://apireference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Used to set the foreground color.
- [**Style.BackgroundThemeColor**](https://apireference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Used to set the background color.
- [**Font.ThemeColor**](https://apireference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Used to set the font color.
- [**Workbook.GetThemeColor**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Used to get a theme color.
- [**Workbook.SetThemeColor**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Used to set a theme color.

The following example shows how to get and set theme colors.

The following example uses a template XLSX file, gets the colors for different theme color types, changes the colors and saves the Microsoft Excel file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

#### **Customize Themes**

The following example shows how to apply custom themes with your desired colors. We use a sample template file manually created in Microsoft Excel 2007.

The following example loads a template XLSX file, defines colors for different theme color types, applies the custom colors and saves the excel file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

#### **Use Theme Colors**

The following example applies a cell’s foreground and font colors based on the default theme (of the workbook) color types. It also saves the excel file to disk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}
