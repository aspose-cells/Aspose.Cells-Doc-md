---
title: Applicare la formattazione condizionale nel foglio di lavoro
type: docs
weight: 40
url: /it/cpp/apply-conditional-formatting-in-worksheet/
---
## **Possibile scenario di utilizzo**
 Aspose.Cells consente di aggiungere tutti i tipi di formattazione condizionale, ad esempio Formula, Sopra la media, Scala colori, Barra dati, Set di icone, Top10, ecc. Fornisce il[IFormatCondition](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition)class che ha tutti i metodi necessari per applicare la formattazione condizionale di tua scelta. Ecco l'elenco di alcuni metodi Get.

- [GetIAsopra la media()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#aff550fd834cd78967ec440492ff012d5)
- [GetIColorScale()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a3348a7c447dc564ceabc22c9c89bd6f5)
- [GetIDDataBar()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a4415a87833c41386ed1595e742485e07)
- [GetIIconSet()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a011b2c7dbaaf671819d09f5d1df865e3)
- [GetITTop10()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a64388aaf1b43811f5ee1ee3090c9bd4a)
## **Applicare la formattazione condizionale nel foglio di lavoro**
 Il codice di esempio seguente mostra come aggiungere una formattazione condizionale Valore Cell nelle celle A1 e B2. Si prega di consultare il[file excel di output](23167004.xlsx) generato dal codice e la seguente schermata che spiega l'effetto del codice sul[file excel di output](23167004.xlsx). Se inserirai un valore maggiore di 100 nelle celle A2 e B2, il colore di riempimento rosso dalle celle A1 e B2 scomparirà.

![cose da fare:immagine_alt_testo](apply-conditional-formatting-in-worksheet_1.png)
## **Codice d'esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet.cpp" >}}
