---
title: القيود و API الاختلافات
type: docs
weight: 10
url: /ar/php-java/limitations-and-api-differences/
keywords: php, excel, limitation, api, difference
description: Aspose.Cells for PHP via Java القيود والاختلافات API
---
## **عام API الاختلافات**


توضح القائمة التالية (مع نماذج مقاطع الكود) بعض الاختلافات بين واجهات برمجة التطبيقات (APIs) Aspose.Cells for Java و Aspose.Cells for PHP via Java واجهات برمجة التطبيقات.
### **مكتبة الاستيراد (مقارنات الحزم)**

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


### **إنشاء مصنف جديد**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells for PHP via Java**

{{< highlight "java" >}}

 $workbook = new Workbook();

{{< /highlight >}}


### **Enums أو الثوابت**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells for PHP via Java**

{{< highlight "java" >}}

 $arc2->getLineFormat()->setDashStyle(cells\MsoLineDashStyle::SOLID);

{{< /highlight >}}


### **مثال**

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


## **قيود أخرى من Aspose.Cells for PHP via Java API مقارنة بـ Aspose.Cells for Java API**
1. لا يتم دعم استيراد / تصدير البيانات من Array و ArrayList و ResultSet وما إلى ذلك.
1. الطباعة غير مدعومة.

