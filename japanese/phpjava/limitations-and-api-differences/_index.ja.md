---
title: 制限事項と API の相違点
type: docs
weight: 10
url: /ja/php-java/limitations-and-api-differences/
keywords: php, excel, limitation, api, difference
description: Aspose.Cells for PHP via Java 制限と API の違い
---
## **公開 API 違い**


次のリスト (サンプル コード セグメント付き) は、Aspose.Cells for Java と Aspose.Cells for PHP via Java API の違いを示しています。
### **ライブラリのインポート (パッケージ比較)**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 import com.aspose.cells.*;

{{< /highlight >}}

**Aspose.Cells for PHP via Java**

{{< highlight "java" >}}

 require_once("Java.inc");

require_once("lib/aspose.cells.php");

use aspose\cells;

use aspose\cells\Workbook;

{{< /highlight >}}


### **新しいワークブックのインスタンス化**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells for PHP via Java**

{{< highlight "java" >}}

 $workbook = new Workbook();

{{< /highlight >}}


### **列挙型または定数**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells for PHP via Java**

{{< highlight "java" >}}

 $arc2->getLineFormat()->setDashStyle(cells\MsoLineDashStyle::SOLID);

{{< /highlight >}}


### **例**

**Aspose.Cells for Java**

{{< highlight "java" >}}

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

{{< highlight "java" >}}

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
1. Array、ArrayList、ResultSet などからのデータのインポート/エクスポートはサポートされていません。
1. 印刷は対応しておりません。

