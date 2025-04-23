---
title: Impostazione della formula per Intervallo con Nome
type: docs
weight: 20
url: /it/python-net/setting-formula-for-named-range/
---

## **Impostazione della formula per il intervallo nominato**
Come l'applicazione Excel, le API di Aspose.Cells for Python via .NET offrono la possibilità di specificare una formula per un intervallo denominato usando la sua proprietà [**Range.refers_to**](https://reference.aspose.com/cells/python-net/aspose.cells/range/refers_to). Ci possono essere numerosi scenari di usabilità per questa funzionalità, alcuni dei quali sono dettagliati di seguito.
### **Impostazione di una Simple Formula per Intervallo con Nome**
Una formula semplice potrebbe essere un riferimento ad un'altra cella nella stessa (o diversa) cartella di lavoro. Nell'esempio seguente viene creato un intervallo con nome in un nuovo foglio di lavoro e si imposta il suo riferimento ad un'altra cella.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSimpleFormulaForNamedRanges.py" >}}
### **Impostazione di una Formula Complessa per Intervallo con Nome**
Una formula complessa potrebbe essere qualsiasi cosa, come un intervallo dinamico o una formula che si estende su più celle in fogli di lavoro diversi. Nell'esempio seguente viene creato un intervallo dinamico utilizzando la funzione INDICE per ottenere il valore da un elenco in base alla sua posizione.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingComplexFormulaNamedRange.py" >}}



Ecco un altro esempio che utilizza un intervallo con nome per sommare i valori di 2 celle in fogli di lavoro diversi.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-CalculatingSumUsingNamedRangeOnDifferentSheets.py" >}}
