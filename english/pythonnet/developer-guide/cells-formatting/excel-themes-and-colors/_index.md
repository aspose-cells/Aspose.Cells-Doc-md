---
title: Excel Themes and Colors
type: docs
weight: 100
url: /python-net/excel-themes-and-colors/
description: C# code to use Excel Color Scheme with Aspose.Cells for Python via .NET API
keywords: C# to Create and Apply Color Schemes, c# programmatically Create a Custom Color Scheme, programmatically how to Apply a Custom Color Scheme, c# how to Use Color Scheme in excel
---

## **How to Apply and Create Color Scheme in Excel**
Document themes make it easy to coordinate colors, fonts, and graphic formatting effects of Excel documents and update them quickly. 
Themes provide a unified look with named styles, graphical effects and other objects used in a workbook. For example, the Accent1 style, for example, looks different in the Office and the Apex themes. Often, you apply a document theme and then amend it to how you want it.

### **How to Apply a Color Scheme in Excel**
1. Open Excel and go to the "Page Layout" tab in the Excel ribbon.
1. Click on the "Colors" button in the "Themes" section.
<br>
<img src="color.png" width=70% />
1. Choose a color palette that matches your requirements or hover over a scheme to see a live preview.

### **How to Create a Custom Color Scheme in Excel**
You can create your own color set to give your document a fresh, unique look or comply with your organization’s brand standards.

1. Open Excel and go to the "Page Layout" tab in the Excel ribbon.
1. Click on the "Colors" button in the "Themes" section.
1. Click "Customize Colors..." button.
<br>
<img src="color2.png" width=70% />

1. In the "Create New Theme Colors" dialog box, you can select colors for each element by clicking on the color dropdowns next to them. You can choose colors from the palette or define custom colors using the "More Colors" option.
<br>
<img src="color3.png" width=70% />
1. After selecting all the desired colors, provide a name for your custom color scheme in the "Name" field.

1. Click on the "Save" button to save your custom color scheme. Your custom color scheme will now be available in the "Colors" drop-down menu for future use.

## **How to Create and Apply Color Scheme in Aspose.Cells for Python via .NET**
Aspose.Cells for Python via .NET provides features for customizing themes and colors.

### **How to Create Custom Color Theme in Aspose.Cells for Python via .NET**
If theme colors are used in the file, we don't need to modify each cell individually, we just need to modify the colors in the theme.

The following example shows how to apply custom themes with your desired colors. We use a sample template file manually created in Microsoft Excel 2007.

The following example loads a template XLSX file, defines colors for different theme color types, applies the custom colors and saves the excel file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CustomizeThemes-1.py" >}}

### **How to Apply Theme Colors in Aspose.Cells for Python via .NET**

The following example applies a cell’s foreground and font colors based on the default theme (of the workbook) color types. It also saves the excel file to disk.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UtilizeThemeColors-1.py" >}}

### **How to Get and Set Theme Colors in Aspose.Cells for Python via .NET**
 Below are a few methods and properties that implement theme colors.

- [**Style.foreground_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_theme_color): Used to set the foreground color.
- [**Style.background_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_theme_color): Used to set the background color.
- [**Font.theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/theme_color): Used to set the font color.
- [**Workbook.get_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/get_theme_color): Used to get a theme color.
- [**Workbook.set_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/set_theme_color): Used to set a theme color.

The following example shows how to get and set theme colors.

The following example uses a template XLSX file, gets the colors for different theme color types, changes the colors and saves the Microsoft Excel file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GetSetThemeColors-1.py" >}}

## **Advance topics**
- [Extract Theme Data from Excel File](/cells/python-net/extract-theme-data-from-excel-file/)

{{< app/cells/assistant language="python-net" >}}