---
title: 限制和API差异
type: docs
weight: 10
url: /zh/php-java/limitations-and-api-differences/
keywords: "php, excel, limitation, api, differences"
description: "Aspose.Cells for PHP via Java限制和API差异。"
---

## **公共API差异**


以下列表（附有代码段示例）显示了Aspose.Cells for Java和Aspose.Cells for PHP via Java API之间的一些差异。
### **导入库（软件包对比）**

**Aspose.Cells for Java**

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}

**Aspose.Cells for PHP via Java**

{{< highlight java >}}

 require_once("Java.inc");

require_once("lib/aspose.cells.php");

use aspose\cells;

use aspose\cells\Workbook;

{{< /highlight >}}


### **实例化新工作簿**

**Aspose.Cells for Java**

{{< highlight java >}}

 Workbook workbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells for PHP via Java**

{{< highlight java >}}

 $workbook = new Workbook();

{{< /highlight >}}


### **枚举或常量**

**Aspose.Cells for Java**

{{< highlight java >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells for PHP via Java**

{{< highlight java >}}

 $arc2->getLineFormat()->setDashStyle(cells\MsoLineDashStyle::SOLID);

{{< /highlight >}}


### **例子**

**Aspose.Cells for Java**

{{< highlight java >}}

 import com.aspose.cells.*;

public class Test1 {

	/**

	 * @param args

	 */

	public static void main(String[] args) throws Exception {



		Workbook workbook = new Workbook();

		WorksheetCollection worksheets = workbook.getWorksheets();

		Worksheet worksheet = worksheets.get(0);

		Cell cell = worksheet.getCells().get("A1");

		cell.putValue("Hello World!");

		workbook.save("out1.xlsx");

	}

}

{{< /highlight >}}





**Aspose.Cells for PHP via Java**

{{< highlight java >}}

 <?php



require_once("Java.inc");

require_once("lib/aspose.cells.php");

use aspose\cells;

use aspose\cells\Workbook;

use aspose\cells\WorsheetCollection;

use aspose\cells\Worksheet;

use aspose\cells\Cell;


$workbook = new Workbook();

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$cell = $worksheet->getCells()->get("A1");

$cell->putValue("Hello World!");

$workbook->save("out1.xlsx");


?>

{{< /highlight >}}


## **与Aspose.Cells for Java API相比，Aspose.Cells for PHP via Java API的其他限制**
1. 不支持从Array、ArrayList、ResultSet等导入/导出数据。
1. 不支持打印。

