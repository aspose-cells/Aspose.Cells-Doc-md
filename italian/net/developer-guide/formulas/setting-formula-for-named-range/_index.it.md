---
title: Impostazione della formula per l'intervallo denominato
type: docs
weight: 20
url: /it/net/setting-formula-for-named-range/
---
## **Impostazione della formula per l'intervallo denominato**
 Come l'applicazione Excel, le API Aspose.Cells offrono la possibilità di specificare una formula per un intervallo denominato durante l'utilizzo del relativo[Si riferisce a](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto)proprietà. Potrebbero esserci numerosi scenari di usabilità per questa funzione, alcuni dei quali sono dettagliati come segue.
### **Impostazione di una formula semplice per un intervallo denominato**
Una formula semplice potrebbe essere un riferimento a un'altra cella nello stesso (o diverso) foglio di lavoro. L'esempio seguente crea un intervallo denominato in un nuovo foglio di calcolo e ne imposta il riferimento a un'altra cella.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **Impostazione di una formula complessa per un intervallo denominato**
Una formula complessa può essere qualsiasi cosa, ad esempio un intervallo dinamico o una formula che si estende su più celle in diversi fogli di lavoro. L'esempio seguente crea un intervallo dinamico utilizzando la funzione INDICE per ottenere il valore da un elenco in base alla sua posizione.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



Ecco un altro esempio che utilizza un intervallo denominato per sommare i valori di 2 celle in diversi fogli di lavoro.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
