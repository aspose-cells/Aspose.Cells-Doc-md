---
title: Applicare formattazione condizionale nel foglio di lavoro
type: docs
weight: 40
url: /it/cpp/apply-conditional-formatting-in-worksheet/
---

## **Scenario di utilizzo possibile**
Aspose.Cells permette di aggiungere tutti i tipi di formattazione condizionale, ad es. Formula, Sopra la media, Scala colore, Barra dati, Serie di icone, Top10, ecc. Fornisce la classe [FormatCondition](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/) che ha tutti i metodi necessari per applicare la formattazione condizionale a tua scelta. Ecco l'elenco di alcuni dei metodi Get.

- [GetAboveAverage()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getaboveaverage/)
- [GetColorScale()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getcolorscale)
- [GetDataBar()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getdatabar)
- [GetIconSet()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/geticonset)
- [GetTop10()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/gettop10)
## **Applicare formattazione condizionale nel foglio di lavoro**
Il seguente codice di esempio mostra come aggiungere una formattazione condizionale del valore della cella sulle celle A1 e B2. Si prega di vedere il [file excel di output](23167004.xlsx) generato dal codice e la seguente schermata che spiega l'effetto del codice sul [file excel di output](23167004.xlsx). Se immetti un valore maggiore di 100 nella cella A2 e B2, il colore di riempimento rosso dalle celle A1 e B2 scomparirà.

![todo:image_alt_text](apply-conditional-formatting-in-worksheet_1.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet-new.cpp" >}}
