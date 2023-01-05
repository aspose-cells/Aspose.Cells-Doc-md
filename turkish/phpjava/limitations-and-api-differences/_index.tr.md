---
title: Sınırlamalar ve API Farklar
type: docs
weight: 10
url: /tr/php-java/limitations-and-api-differences/
keywords: php, excel, limitation, api, difference
description: Aspose.Cells for PHP via Java kısıtlamalar ve api farklılıkları
---
## **Kamu API Farklar**


Aşağıdaki liste (örnek kod segmentleriyle birlikte), Aspose.Cells for Java ve Aspose.Cells for PHP via Java API'ler arasındaki bazı farklılıkları göstermektedir.
### **Kitaplığı içe aktarma (Paket Karşılaştırmaları)**

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


### **Yeni bir Çalışma Kitabı örneği oluşturma**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells for PHP via Java**

{{< highlight "java" >}}

 $workbook = new Workbook();

{{< /highlight >}}


### **Numaralandırmalar veya Sabitler**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells for PHP via Java**

{{< highlight "java" >}}

 $arc2->getLineFormat()->setDashStyle(cells\MsoLineDashStyle::SOLID);

{{< /highlight >}}


### **Örnek vermek**

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


## **Aspose.Cells for PHP via Java API'in Aspose.Cells for Java API ile karşılaştırıldığında Diğer Sınırlamaları**
1. Array, ArrayList, ResultSet vb.'den veri içe/dışa aktarma desteklenmez.
1. Yazdırma desteklenmiyor.

