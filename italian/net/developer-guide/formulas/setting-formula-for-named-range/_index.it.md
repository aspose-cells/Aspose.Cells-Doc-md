---
title: Impostazione della formula per Intervallo con Nome
type: docs
weight: 20
url: /it/net/setting-formula-for-named-range/
---

## **Impostazione della formula per il intervallo nominato**
Come l'applicazione Excel, le API di Aspose.Cells forniscono la possibilità di specificare una formula per un intervallo con nome utilizzando la proprietà [RefersTo](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto). Ci potrebbero essere numerose situazioni d'uso per questa funzionalità, alcune delle quali dettagliate di seguito.
### **Impostazione di una Simple Formula per Intervallo con Nome**
Una formula semplice potrebbe essere un riferimento ad un'altra cella nella stessa (o diversa) cartella di lavoro. Nell'esempio seguente viene creato un intervallo con nome in un nuovo foglio di lavoro e si imposta il suo riferimento ad un'altra cella.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **Impostazione di una Formula Complessa per Intervallo con Nome**
Una formula complessa potrebbe essere qualsiasi cosa, come un intervallo dinamico o una formula che si estende su più celle in fogli di lavoro diversi. Nell'esempio seguente viene creato un intervallo dinamico utilizzando la funzione INDICE per ottenere il valore da un elenco in base alla sua posizione.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



Ecco un altro esempio che utilizza un intervallo con nome per sommare i valori di 2 celle in fogli di lavoro diversi.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
{{< app/cells/assistant language="csharp" >}}
