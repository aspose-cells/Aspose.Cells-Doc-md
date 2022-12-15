---
title: Aspose.Cells for Java 16.10.0 Note di rilascio
type: docs
weight: 30
url: /it/java/aspose-cells-for-java-16-10-0-release-notes/
---
## **1) Aspose.Cells**

|**Chiave** |**Riepilogo** |**Categoria** |
|:- |:- |:- |
|CELLSJAVA-41974 | L'aggiornamento della tabella pivot non funziona nel file PDF sottoposto a rendering| Insetto|
|CELLSJAVA-41900 | XLSM viene danneggiato da una semplice operazione di caricamento e salvataggio| Insetto|
|CELLSJAVA-41790 | I collegamenti ipertestuali non funzionano come previsto dopo la conversione del foglio di calcolo in HTML| Insetto|
|CELLSJAVA-42010 | Alcuni caratteri non vengono visualizzati nel PDF di output| Insetto|
|CELLSJAVA-41977 | Ordine della legenda del grafico modificato nel PDF del grafico| Insetto|
|CELLSJAVA-41972 | L'ordine Z delle righe alto-basso non è corretto nel PDF| Insetto|
|CELLSJAVA-42015 | Il foglio di calcolo viene danneggiato dopo il nuovo salvataggio con Aspose.Cells| Insetto|
|CELLSJAVA-42005 | La formula viene modificata dopo l'inserimento in una cella| Insetto|
|CELLSJAVA-41997 | Strano comportamento con il fagiolo semplice utilizzando gli Smart Markers| Insetto|
|CELLSJAVA-41993 | NullPointerException durante l'apertura di un file a7.xlsm| Eccezione|
|CELLSJAVA-41992 | NullPointerException durante l'apertura di un file a6.xlsm| Eccezione|
|CELLSJAVA-41991 |NullPointerException durante l'apertura di un file a5.xlsm| Eccezione|
|CELLSJAVA-41990 | NullPointerException durante l'apertura di un file a4.xlsm| Eccezione|
|CELLSJAVA-41989 | NullPointerException durante l'apertura di un file a3.xlsm| Eccezione|
|CELLSJAVA-41988 | NullPointerException durante l'apertura di un file a2.xlsm| Eccezione|
|CELLSJAVA-41987 | NullPointerException durante l'apertura di un file a1.xlsm| Eccezione|
|CELLSJAVA-41968 | IndexOutOfBoundsException: Index: 23, Size: 14 durante l'aggiornamento del grafico pivot| Eccezione|
|CELLSJAVA-42014 | ClassCastException: com.aspose.cells.zadp non può essere trasmesso a com.aspose.cells.zadq durante il nuovo salvataggio di XLSX| Eccezione|
## **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà Shape.Reflection e la classe ReflectionEffect**
Rappresenta l'effetto riflesso per l'elemento o la forma del grafico.
### **Aggiunge le proprietà Shape.Glow, GlowEffect.Size e GlowEffect.Transparency**
Rappresenta l'effetto bagliore per l'elemento o la forma del grafico.
### **Aggiunge l'enumerazione LightRigType.None**
Non rappresenta alcuna impostazione di illuminazione.
### **Aggiunge la proprietà Shape.ShadowEffect**
Rappresenta l'effetto ombra per l'elemento o la forma del grafico.
### **Aggiunge la proprietà ExternalLink.IsVisible**
Indica se il collegamento esterno è visibile.
### **Aggiunge la proprietà Shape.ThreeDFormat e la classe ThreeDFormat**
Ottiene e imposta il formato 3D della forma.
### **Aggiunge l'enumerazione PresetCameraType**
Rappresenta diversi metodi algoritmici per l'impostazione di tutte le proprietà della telecamera, inclusa la posizione.
### **Aggiunge l'enumerazione LightRigDirectionType**
Rappresenta il tipo di direzione dell'impianto luci.
### **Aggiunge l'enumerazione BevelType**
Rappresenta un preset per un tipo di smusso che può essere applicato a una forma in 3D.
### **Aggiunge il metodo XmlMapCollection.Add(string url).**
Aggiunge un XmlMap in base all'URL/percorso di un file XML.
### **Aggiunge il metodo ShapeCollection.AddWordArt() e l'enumerazione PresetWordArtStyle**
Aggiunge WordArt preimpostato da MS Excel 2007.
### **Aggiunge il metodo FontSettingCollection.SetWordArtStyle() e il metodo FontSetting.SetWordArtStyle()**
Imposta lo stile WordArt preimpostato sul testo della forma.
### **Aggiunge il metodo Cells.LinkToXmlMap(string mapName, int row, int column, string path)**
Collegamento a una mappa xml.
### **Aggiunge la proprietà ListColumn.Formula**
Ottiene e imposta la formula della colonna elenco.
### **Aggiunge la proprietà GridWeb.CustomCalculationEngine e la classe GridAbstractCalculationEngine**
Rappresenta il motore di calcolo personalizzato dell'utente per estendere il motore di calcolo predefinito di Aspose.Cells.GridWeb.
