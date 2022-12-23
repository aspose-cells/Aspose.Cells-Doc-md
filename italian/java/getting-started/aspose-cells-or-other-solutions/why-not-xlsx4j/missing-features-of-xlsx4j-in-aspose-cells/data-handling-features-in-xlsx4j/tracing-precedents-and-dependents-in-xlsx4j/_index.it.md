---
title: Tracciamento di precedenti e dipendenti in xlsx4j
type: docs
weight: 70
url: /it/java/tracing-precedents-and-dependents-in-xlsx4j/
---
## **Aspose.Cells - Rintraccio Precedenti e Dipendenti**
Fogli di lavoro finanziari complessi, specialmente quelli sviluppati in collaborazione, possono nascondere gli errori più imbarazzanti. Controllare l'accuratezza delle formule e trovare l'origine di un errore può essere difficile quando la formula utilizza celle precedenti e celle dipendenti.

- **Cellule precedenti**sono celle a cui fa riferimento una formula in un altro Cell. Ad esempio, se la cella D10 contiene la formula =B5, la cella B5 è precedente alla cella D10.
- **Cellule dipendenti**contengono formule che fanno riferimento ad altre celle. Ad esempio, se la cella D10 contiene la formula =B5, la cella D10 dipende dalla cella B5.

Per rendere il foglio di calcolo facile da leggere, potresti voler mostrare chiaramente quali celle di un foglio di calcolo vengono utilizzate in una formula. Allo stesso modo, potresti voler estrarre le celle dipendenti di altre celle.

Aspose.Cells permette di rintracciare le celle e scoprire quali sono collegate.

Rintracciare i precedenti

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook(dataDir + "workbook.xls");

Cells cells = workbook.getWorksheets().get(0).getCells();

Cell cell = cells.get("A12");

//Tracing precedents of the cell A12.

//The return array contains ranges and cells.

ReferredAreaCollection ret = cell.getPrecedents();

//Printing all the precedent cells' name.

if(ret != null)

{

  for(int m = 0 ; m < ret.getCount(); m++)

  {

    ReferredArea area = ret.get(m);

    StringBuilder stringBuilder = new StringBuilder();

    if (area.isExternalLink())

    {

        stringBuilder.append("[");

        stringBuilder.append(area.getExternalFileName());

        stringBuilder.append("]");

     }

     stringBuilder.append(area.getSheetName());

     stringBuilder.append("!");

     stringBuilder.append(CellsHelper.cellIndexToName(area.getStartRow(), area.getStartColumn()));

     if (area.isArea())

      {

          stringBuilder.append(":");

          stringBuilder.append(CellsHelper.cellIndexToName(area.getEndRow(), area.getEndColumn()));

      }

      System.out.println("Tracing Precedents: " + stringBuilder.toString());

   }

}

{{< /highlight >}}

Tracciamento dei dipendenti

**Java**

{{< highlight "java" >}}

 //Prendi la cella A1

Cell c = celle.get("A5");

//Prendi tutti i dipendenti della cella A5

Cell[]dipendenti = c.getDependents(true);

per (int i = 0; i< dependents.length; i++)

{

     System.out.println("Tracing Dependents: " + dependents[i].getWorksheet().getName() +dependents[i].getName() + ":" + dependents[i].getIntValue());

}

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/tracingprecedentsanddependents/AsposeTracingPrecedentsAndDependents.java)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Rintracciare precedenti e dipendenti](/java/tracing-precedents-and-dependents).

{{% /alert %}}
