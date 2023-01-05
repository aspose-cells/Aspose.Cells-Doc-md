---
title: Limites et différences API
type: docs
weight: 10
url: /fr/php-java/limitations-and-api-differences/
keywords: php, excel, limitation, api, difference
description: Aspose.Cells for PHP via Java limitations et différences API
---
## **Publique API Différences**


La liste suivante (avec des exemples de segments de code) montre certaines différences entre les API Aspose.Cells for Java et Aspose.Cells for PHP via Java.
### **Importation de la bibliothèque (comparaisons de packages)**

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


### **Instanciation d'un nouveau classeur**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells for PHP via Java**

{{< highlight "java" >}}

 $workbook = new Workbook();

{{< /highlight >}}


### **Énumérations ou constantes**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells for PHP via Java**

{{< highlight "java" >}}

 $arc2->getLineFormat()->setDashStyle(cells\MsoLineDashStyle::SOLID);

{{< /highlight >}}


### **Exemple**

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


## **Autres limitations de Aspose.Cells for PHP via Java API par rapport à Aspose.Cells for Java API**
1. L'importation/exportation de données à partir d'un Array, ArrayList, ResultSet, etc. n'est pas prise en charge.
1. L'impression n'est pas prise en charge.

