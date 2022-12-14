---
title: Sınırlamalar ve API Farklar
type: docs
weight: 10
url: /tr/php-java/limitations-and-api-differences/
keywords: php, excel, limitation, api, difference
description: Java sınırlamaları ve api farklılıkları aracılığıyla PHP için Aspose.Cells
---
## **Kamu API Farklar**


Aşağıdaki liste (örnek kod bölümleriyle birlikte), Java API'leri aracılığıyla PHP için Aspose.Cells for Java ve Aspose.Cells arasındaki bazı farklılıkları göstermektedir.
### **Kitaplığı içe aktarma (Paket Karşılaştırmaları)**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 import com.aspose.cells.*;

{{< /highlight >}}

**Java aracılığıyla PHP için Aspose.Cells**

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


**Java aracılığıyla PHP için Aspose.Cells**

{{< highlight "java" >}}

 $workbook = new Workbook();

{{< /highlight >}}


### **Numaralandırmalar veya Sabitler**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Java aracılığıyla PHP için Aspose.Cells**

{{< highlight "java" >}}

 $arc2->getLineFormat()->setDashStyle(cells\MsoLineDashStyle::SOLID);

{{< /highlight >}}


### **Örnek**

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





**Java aracılığıyla PHP için Aspose.Cells**

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


## **Java API aracılığıyla PHP için Aspose.Cells'in Diğer Sınırlamaları, Aspose.Cells for Java API ile karşılaştırıldığında**
1. Array, ArrayList, ResultSet vb.'den veri içe/dışa aktarma desteklenmez.
1. Yazdırma desteklenmiyor.

