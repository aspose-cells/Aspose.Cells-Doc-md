---
title: 制限とAPIの違い
type: docs
weight: 10
url: /ja/php-java/limitations-and-api-differences/
keywords: "php, excel, limitation, api, differences"
description: "Aspose.Cells for PHP via Java の制限とAPIの違い"
---

## **公開APIの違い**


以下のリスト（サンプルコードセグメント付き）は、Aspose.Cells for JavaとAspose.Cells for PHP via JavaのAPIの一部の違いを示しています。
### **ライブラリの読み込み（Package Comparisons）**

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


### **新しいワークブックのインスタンス化**

**Aspose.Cells for Java**

{{< highlight java >}}

 Workbook workbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells for PHP via Java**

{{< highlight java >}}

 $workbook = new Workbook();

{{< /highlight >}}


### **列挙型または定数**

**Aspose.Cells for Java**

{{< highlight java >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells for PHP via Java**

{{< highlight java >}}

 $arc2->getLineFormat()->setDashStyle(cells\MsoLineDashStyle::SOLID);

{{< /highlight >}}


### **例**

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


## **Aspose.Cells for PHP via Java API と Aspose.Cells for Java API のその他の制限事項**
1. 配列、ArrayList、ResultSet などからのデータのインポート/エクスポートはサポートされていません。
1. プリントはサポートされていません。

