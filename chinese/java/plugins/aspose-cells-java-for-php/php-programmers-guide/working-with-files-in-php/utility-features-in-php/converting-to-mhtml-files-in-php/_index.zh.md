---
title: 在 PHP 中转换为 MHTML 文件
type: docs
weight: 40
url: /zh/java/converting-to-mhtml-files-in-php/
---
## **Aspose.Cells - 转换为 MHTML 文件**
要在 PHP 中使用 Aspose.Cells for Java 将工作表转换为 MHTML 文件，只需调用工作表_至_Converter 模块的 mhtml() 方法。

**PHP代码**

{{< highlight "php" >}}

 $sveFormat = new SaveFormat();

//Specify the file path

$filePath = $dataDir . "Book1.xlsx";

//Specify the HTML saving options

$sv = new HtmlSaveOptions($sveFormat->M_HTML);

//Instantiate a workbook and open the template XLSX file

$wb = new Workbook($filePath);

//Save the MHT file

$wb->save($filePath . ".out.mht", $sv);

{{< /highlight >}}
## **下载运行代码**
下载**转换为 MHTML 文件 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)
