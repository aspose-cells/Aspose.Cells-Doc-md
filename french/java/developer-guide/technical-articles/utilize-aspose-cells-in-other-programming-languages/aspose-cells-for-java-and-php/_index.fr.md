---
title: Aspose.Cells for Java and PHP
type: docs
weight: 20
url: /fr/java/aspose-cells-for-java-and-php/
---

{{% alert color="primary" %}} 

Les développeurs PHP peuvent utiliser Aspose.Cells for Java dans les applications PHP. Pour travailler avec Aspose.Cells for Java et PHP, utilisez la version PHP 5 (connue sous le nom de PHP5). PHP4 peut également être utilisé pour accéder à Aspose.Cells for Java mais c'est plus complexe que d'utiliser PHP5. 

{{% /alert %}} 
## **Travailler avec PHP**
### **Utiliser PHP5**
Aspose.Cells for Java fournit des classes wrappers PHP5 qui facilitent l'utilisation de la bibliothèque Aspose.Cells sans travailler directement avec les classes Java. 

Ces classes wrappers se trouvent dans le répertoire PHP de l'archive aspose.cells.zip sous forme d'un fichier PHP. 
## **Utiliser PHP4**
PHP4 fonctionne également avec Aspose.Cells for Java, mais dans ce cas, les développeurs devront travailler directement avec les classes Java. 

{{% alert color="primary" %}} 

N'oubliez pas d'ajouter aspose.cells.jar à java.class.path dans le fichier php.ini. 

Les classes enveloppes PHP fournissent des méthodes statiques pour créer des classes PHP pour la classe Java correspondante, dans la ClassFactory avec la signature createXXX(). Si les constructeurs sont surchargés, toutes les méthodes correspondantes dans la ClassFactory sont définies comme create+numéro de série+nom de classe, par exemple : ((createXXX()}, create1XXX(args...), create2XXX(args...), et ainsi de suite. 

Toutes les constantes sont définies en PHP comme ClassName+" "+ConstantName, par exemple, BorderLineType.NONE est défini comme BorderLineType NONE en PHP. 

Si les méthodes sont surchargées, elles sont définies comme nom de méthode + numéro de série, par exemple cell.setValue, cell.setValue1(), cell.setValue2(), et ainsi de suite. 

La méthode clone() est définie comme cloneObject(). 

{{% /alert %}} 

**PHP**

{{< highlight csharp >}}

 <?php

require_once("java/Java.inc");

require("AsposeCells.php");

$workbook = ClassFactory::createWorkbook();

$workbook->open5("t1.xls");

$cell = $workbook->getWorksheets()->get(0)->getCells()->getCell(0, 0);

$cell->setValue6("Hello World!"); 

$workbook->save5("t.xls");

?>



{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
