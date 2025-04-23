# Libreria Go per formati di file Excel

![Versione 24.11.0](https://img.shields.io/badge/go-v24.11.0-blue)

[Pagina del prodotto](https://products.aspose.com/cells/go-cpp/) | [Documentazione](https://docs.aspose.com/cells/go-cpp/) | [Demos](https://products.aspose.app/cells/family) | [Riferimento API](https://reference.aspose.com/cells/go-cpp) | [Esempi](https://github.com/aspose-cells/aspose-cells-go-cpp) | [Blog](https://blog.aspose.com/category/cells/) | [Rilasci](https://releases.aspose.com/cells/go-cpp/) | [Supporto gratuito](https://forum.aspose.com/c/cells) | [Licenza temporanea](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for Go via C++](https://products.aspose.com/cells/go-cpp/) è una libreria Go nativa per creare, manipulare, processare e convertire file Microsoft Excel senza bisogno di Microsoft Office o Automazione. L'API Excel Go supporta Excel 97-2003 (XLS), Excel 2007-2013/2016 (XLSX, XLSM, XLSB), OpenOffice XML e altri formati come CSV, TSV e altro ancora.

Consente agli sviluppatori di lavorare con righe, colonne, dati, formule, tabelle pivot, fogli di lavoro, tabelle, grafici e oggetti di disegno dai loro applicazioni Go.

## Cos'è Aspose.Cells for Go via C++?

Aspose.Cells for Go via C++ è un'API nativa Go on premise per integrare le funzionalità di creazione, manipolazione e conversione di fogli di calcolo nelle tue applicazioni Go. Supporta la lavorazione con molti formati di file di fogli di calcolo popolari di Microsoft Excel (XLS, XLSX, XLSB, CSV, ecc.) e OpenOffice/LibreOffice (ODS).

Puoi usare Aspose.Cells for Go via C++ per sviluppare applicazioni a 64 bit in qualsiasi ambiente di sviluppo che supporti Go, come ad esempio Microsoft Visual Studio. Aspose.Cells for Go via C++ è un assembly nativo che può essere distribuito semplicemente copiandolo. Non è necessario preoccuparsi di altri servizi o moduli.

Aspose.Cells for Go via C++ ti permette di lavorare con le proprietà del documento integrate e personalizzate in Microsoft Excel. Supporta la conversione di alta qualità dei workbook di Excel in file compatibili PDF/A. Lavora con formule, tabelle pivot, fogli di lavoro, tabelle, intervalli, grafici, oggetti OLE e molto altro.

## Funzionalità di elaborazione file Excel

- Aprire un file di foglio di calcolo senza Microsoft Excel.
- [Apri un file Excel](https://docs.aspose.com/cells/go/different-ways-to-open-files/) tramite un percorso sul computer locale o usando uno stream.
- [Converti un foglio di lavoro](https://docs.aspose.com/cells/go/converting-worksheet-to-different-image-formats/) in diversi formati di immagine.
- [Applica formattazione condizionale](https://docs.aspose.com/cells/go/apply-conditional-formatting-in-worksheet/) secondo le tue scelte.
- [Manipola tabelle pivot](https://docs.aspose.com/cells/go/manipulate-pivot-table/) nei tuoi fogli di calcolo.
- [Converti la tabella in intervallo](https://docs.aspose.com/cells/go/tables-and-ranges/) senza perdere la formattazione.
- Recupera il nome di una cella fornendo l'indice di riga e colonna, oppure, [recupera l'indice di riga e colonna della cella](https://docs.aspose.com/cells/go/names-and-indices/) dal suo nome.
- Crea un [grafico a piramide, a linee, a bolla](https://docs.aspose.com/cells/go/creating-and-customizing-charts/), o un grafico personalizzato.
- [Renderizza](https://docs.aspose.com/cells/go/chart-rendering/) i tipi di grafico supportati in immagini o PDF.
- [Inserisci un oggetto OLE nel foglio di lavoro](https://docs.aspose.com/cells/go/inserting-ole-objects-into-the-worksheet/).
- Accedi a tutti gli oggetti OLE contenuti nel foglio di lavoro per [estrazione](https://docs.aspose.com/cells/go/extracting-ole-objects-from-worksheet/).

## Formati di lettura e scrittura supportati

**Microsoft Excel:** XLS, XLSX, XLSB, SpreadsheetML\
**Text:** CSV, TSV, TabDelimited\
**OpenDocument:** ODS\
**Altro:** HTML, MHTML

## Salva documenti di fogli di calcolo come

**Microsoft Excel:** XLSM, XLTX, XLTM, XLAM\
**Formato documento portatile:** PDF, XPS
**Text:** CSV, TSV, TabDelimited\
**Immagini:** SVG, JPEG, PNG, BMP, GIF\
**Web:** HTML, MHTML\
**Metafile:** EMF\
**Altro** DIF

## Cominciare

Sei pronto per provare Aspose.Cells for Go via C++? Basta eseguire `go get -u github.com/aspose-cells/aspose-cells-go-cpp` e importare `github.com/aspose-cells/aspose-cells-go-cpp` dal file go. Se hai già Aspose.Cells for Go via C++ e desideri aggiornare la versione, esegui `go get github.com/aspose-cells/aspose-cells-go-cpp@v24.12.0` per ottenere l'ultima versione.

### Converti XLS in XLSX, XLSB e CSV usando Go

Prova ad eseguire lo snippet sottostante per vedere come funziona l'API nel tuo ambiente o consulta il [Repository GitHub](https://github.com/aspose-cells/aspose-cells-go-cpp) per altri scenari di utilizzo comuni.

```Go
lic, _ := NewLicense()
lic.SetLicense_String(os.Getenv("LicensePath"))
workbook, err1 := NewWorkbook_String("Book1.xlsx")
if err1 != nil {
    println(err1)
}
workbook.Save_String("Book1.pdf")
workbook.Save_String("Book1.png")
workbook.Save_String("Book1.txt")
workbook.Save_String("Book1.ods")
workbook.Save_String("Book1.md")
workbook.Save_String("Book1.json")
workbook.Save_String("Book1.html")
```

### Crea un grafico Excel personalizzato con Go

```Go
package main

import (
 . "asposecells"
 "os"
)

func main() {
 lic, _ := NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

 workbook, _ := NewWorkbook()
 worksheets, _ := workbook.GetWorksheets()
 worksheet, _ := worksheets.Get_Int(0)
 cells, _ := worksheet.GetCells()
 cell, _ := cells.Get_String("A1")
 cell.PutValue_Int(50)
 cell, _ = cells.Get_String("A2")
 cell.PutValue_Int(100)
 cell, _ = cells.Get_String("A3")
 cell.PutValue_Int(150)
 cell, _ = cells.Get_String("B1")
 cell.PutValue_Int(4)
 cell, _ = cells.Get_String("B2")
 cell.PutValue_Int(20)
 cell, _ = cells.Get_String("B3")
 cell.PutValue_Int(50)
 charts, _ := worksheet.GetCharts()
 chartIndex, _ := charts.Add_ChartType_Int_Int_Int_Int(ChartType_Pyramid, 5, 0, 20, 8)
 chart, _ := charts.Get_Int(chartIndex)
 series, _ := chart.GetNSeries()
 series.Add_String_Bool("A1:B3", true)
 workbook.Save_String("CreateChart.xlsx")
}

```

[Pagina del prodotto](https://products.aspose.com/cells/go-cpp/) | [Documentazione](https://docs.aspose.com/cells/go-cpp/) | [Demos](https://products.aspose.app/cells/family) | [Riferimento API](https://reference.aspose.com/cells/go-cpp) | [Esempi](https://github.com/aspose-cells/aspose-cells-go-cpp) | [Blog](https://blog.aspose.com/category/cells/) | [Rilasci](https://releases.aspose.com/cells/go-cpp/) | [Supporto gratuito](https://forum.aspose.com/c/cells) | [Licenza temporanea](https://purchase.aspose.com/temporary-license/)
