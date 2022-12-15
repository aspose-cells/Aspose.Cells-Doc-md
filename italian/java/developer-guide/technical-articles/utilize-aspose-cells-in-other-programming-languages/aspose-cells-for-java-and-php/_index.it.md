---
title: Aspose.Cells for Java e PHP
type: docs
weight: 20
url: /it/java/aspose-cells-for-java-and-php/
---
{{% alert color="primary" %}} 

 Gli sviluppatori PHP possono utilizzare Aspose.Cells for Java nelle applicazioni PHP. Per lavorare con Aspose.Cells for Java e PHP, utilizzare la versione 5 di PHP (nota come PHP5). PHP4 può anche essere utilizzato per accedere a Aspose.Cells for Java ma è più complesso rispetto all'utilizzo di PHP5.

{{% /alert %}} 
## **Lavorare con PHP**
### **Utilizzando PHP5**
 Aspose.Cells for Java fornisce classi wrapper PHP5 che semplificano agli sviluppatori l'utilizzo della libreria Aspose.Cells senza lavorare direttamente con le classi Java.

 Queste classi wrapper possono essere trovate nella directory PHP dell'archivio aspose.cells.zip sotto forma di file PHP.
## **Utilizzando PHP4**
 PHP4 funziona anche con Aspose.Cells for Java ma in questo caso gli sviluppatori dovrebbero lavorare direttamente con le classi Java.

{{% alert color="primary" %}} 

 Non dimenticare di aggiungere aspose.cells.jar a java.class.path nel file php.ini.

 Le classi wrapper PHP forniscono alcuni metodi statici per creare classi PHP per la corrispondente classe Java, nella ClassFactory con firma createXXX(). Se i costruttori sono sovraccaricati, tutti i metodi corrispondenti in ClassFactory sono definiti come create+numero di serie+nome classe, ad esempio: ((createXXX()}}, create1XXX(args...), create2XXX(args...), e così via.

Tutte le costanti sono definite in PHP come ClassName+" "+ConstantName, ad esempio, BorderLineType.NONE è definito come BorderLineType NONE in PHP.

 Se i metodi sono sovraccaricati, vengono definiti come nome del metodo + numero di serie, ad esempio cell.setValue, cell.setValue1(), cell.setValue2() e così via.

 Il metodo clone() è definito come cloneObject().

{{% /alert %}} 

**PHP**

{{< highlight "csharp" >}}

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
