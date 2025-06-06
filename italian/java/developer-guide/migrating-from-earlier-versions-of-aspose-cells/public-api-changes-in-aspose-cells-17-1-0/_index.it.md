---
title: Modifiche API pubbliche in Aspose.Cells 17.1.0
type: docs
weight: 380
url: /it/java/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 16.12.0 alla 17.1.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per Excel 2016 Grafici**
Aspose.Cells APIs hanno aggiunto il supporto per alcuni grafici di Excel 2016 migliorando l'enumerazione ChartType. I seguenti nuovi campi sono stati aggiunti con il rilascio di Aspose.Cells 17.1.0.

- ChartType.BOX_WHISKER: La serie è disegnata come box and whisker.
- ChartType.FUNNEL: La serie è disegnata come un imbuto.
- ChartType.PARETO_LINE: La serie è disposta come linee di Pareto.
- ChartType.SUNBURST: La serie è disposta come sunburst.
- ChartType.TREEMAP: La serie è disposta come una mappa a blocchi.
- ChartType.WATERFALL: La serie è disposta come un waterfall.
- ChartType.HISTOGRAM: La serie è disposta come un istogramma.

{{% alert color="primary" %}} 

Controlla l'articolo dettagliato su [Lettura Tipi di Grafico Excel 2016](/cells/it/java/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Aggiunto Setter per la Proprietà LoadFilter.LoadDataFilterOptions**
Aspose.Cells 17.1.0 ha aggiunto il setter per la proprietà LoadFilter.LoadDataFilterOptions per sostituire la variabile di istanza m_LoadDataFilterOptions. Gli utenti possono modificare la proprietà LoadDataFilterOptions nella propria implementazione della classe LoadFilter per cambiare il comportamento del caricamento dei file di modello.

Ecco uno scenario d'uso semplice.

{{% alert color="primary" %}} 

Controlla l'articolo dettagliato su [Filtri di Template Personalizzati](/cells/it/java/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 class CustomLoadFilter extends LoadFilter {

	public void startSheet(Worksheet sheet) {

		if (sheet.getName().equals("NoCharts")) {

			//Load everything and filter charts

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CHART);

		}

		if (sheet.getName().equals("NoShapes")) {

			//Load everything and filter shapes

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.SHAPE);

		}

		if (sheet.getName().equals("NoConditionalFormatting")) {

			//Load everything and filter conditional formatting

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CONDITIONAL_FORMATTING);

		}

	}

}

{{< /highlight >}}
### **Aggiunta della proprietà CellsHelper.SignificantDigits**
Aspose.Cells 17.1.0 ha esposto la proprietà SignificantDigits dalla classe CellsHelper che consente di ottenere o impostare il numero di cifre significative per i valori numerici in un foglio di calcolo. Il valore predefinito della proprietà CellsHelper.SignificantDigits è 17 ed è applicabile solo se il risultato deve essere memorizzato nel formato file XLSX.

Ecco uno scenario semplice per dimostrare l'uso della proprietà CellsHelper.SignificantDigits.

{{% alert color="primary" %}} 

Consulta l'articolo dettagliato su [Impostazione del numero di cifre significative](/cells/it/java/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **Aggiunta della proprietà GlowEffect.Color**
Aspose.Cells 17.1.0 ha aggiunto la proprietà GlowEffect.Color che può essere utilizzata per recuperare il colore dell'effetto glow.

Il seguente snippet utilizza la proprietà GlowEffect.Color.

{{% alert color="primary" %}} 

Consulta l'articolo dettagliato su [Lettura del colore della luce di sfondo della forma](/cells/it/java/read-color-of-the-shape-s-glow-effect/)
{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Read the source Excel file

Workbook book = new Workbook(dir + "sample.xlsx");

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access the first shape

Shape shape = sheet.getShapes().get(0);

//Read the glow effect color

GlowEffect glow = shape.getGlow();

CellsColor color = glow.getColor();

{{< /highlight >}}
### **Aggiunte le proprietà PaperWidth e PaperHeight di PageSetup**
Aspose.Cells 17.1.0 ha esposto le proprietà PaperWidth e PaperHeight per la classe PageSetup. Le proprietà PageSetup.PaperWidth e PageSetup.PaperHeight sono di tipo double e rappresentano la larghezza e l'altezza della carta in unità di pollici, considerando l'orientamento della pagina.

{{% alert color="primary" %}} 

Consulta l'articolo dettagliato su [Recupero delle dimensioni della carta del foglio di lavoro](/cells/it/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)

{{% /alert %}} 
### **Aggiunta della proprietà WorkbookSettings.CheckCustomNumberFormat**
Aspose.Cells 17.1.0 ha aggiunto la proprietà CheckCustomNumberFormat alla classe WorkbookSettings. CheckCustomNumberFormat è utile per verificare se la proprietà Style.Custom è stata impostata correttamente o meno. Nel caso in cui la proprietà Style.Custom sia stata impostata in modo improprio, cioè il valore non corrisponde a un modello valido, le API di Aspose.Cells genereranno una CellsException con un messaggio appropriato.

{{% alert color="primary" %}} 

Consulta l'articolo dettagliato su [Verifica formato numerico personalizzato](/cells/it/java/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Set CheckCustomNumberFormat property to true

book.getSettings().setCheckCustomNumberFormat(true);

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access a cell

Cell cell = sheet.getCells().get("B5");

//Insert a value to the cell

cell.putValue(2347);

//Access cell's style

Style style = cell.getStyle();



//Set Custom property to an invalid pattern

style.setCustom("ggg @ fff");

//Set the modified style to the cell

cell.setStyle(style);

{{< /highlight >}}
### **Aggiunta del campo DisplayUnitType.PERCENTAGE**
Aspose.Cells 17.1.0 ha esposto anche il campo PERCENTAGE nell'enumerazione DisplayUnitType. Il campo DisplayUnitType.PERCENTAGE indica che i valori nel grafico devono essere divisi per 0,01.
## **API rimosse**
### **Rimosso la variabile di istanza m_LoadDataFilterOptions**
Questa versione ha rimosso la variabile di istanza m_LoadDataFilterOptions. Si consiglia di utilizzare invece la proprietà LoadFilter.LoadDataFilterOptions.
{{< app/cells/assistant language="java" >}}
