---
title: Impostazioni numeriche con C++
linktitle: Impostazioni numero
description: Aspose.Cells è una libreria C++ per lavorare con file di fogli di calcolo che supporta molte impostazioni numeriche delle celle. Questo articolo introdurrà come usare la libreria Aspose.Cells per gestire le impostazioni dei numeri delle celle, in modo che gli utenti possano regolare il formato dei numeri nel foglio di calcolo secondo necessità.
keywords: Aspose.Cells, libreria C++, foglio di calcolo elettronico, impostazioni numeriche delle celle, formattazione, gestione, formati di numeri e date
type: docs
weight: 10
url: /it/cpp/cells-number-settings/
---

## **Come impostare i formati di visualizzazione dei numeri e delle date**

Una caratteristica molto forte di Microsoft Excel è che consente agli utenti di impostare i formati di visualizzazione dei valori numerici e delle date. Sappiamo che i dati numerici possono essere utilizzati per rappresentare valori diversi, inclusi valori decimali, valute, percentuali, frazioni o valori contabili, ecc. Tutti questi valori numerici vengono visualizzati in formati diversi a seconda del tipo di informazione che rappresentano. Allo stesso modo, ci sono molti formati in cui una data o un'ora possono essere visualizzate.
Aspose.Cells supporta questa funzionalità e consente agli sviluppatori di impostare qualsiasi formato di visualizzazione per un numero o una data.

### **Come impostare i formati di visualizzazione in Microsoft Excel**

Per impostare i formati di visualizzazione in Microsoft Excel:

1. Fai clic con il pulsante destro del mouse su qualsiasi cella.
1. Seleziona **Formato celle**. Comparirà una finestra di dialogo che servirà per impostare i formati di visualizzazione di qualsiasi tipo di valore.

Nella parte sinistra della finestra di dialogo, ci sono molte categorie di valori come **Generale**, **Numero**, **Valuta**, **Contabilità**, **Data**, **Ora**, **Percentuale**, ecc. Aspose.Cells supporte tutti questi formati di visualizzazione.

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso a ogni foglio di lavoro nel file di Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Ciascun elemento della raccolta [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells fornisce i metodi [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) e [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) per la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Questi metodi vengono utilizzati per ottenere e impostare la formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) fornisce alcune proprietà utili per gestire i formati di visualizzazione di numeri e date.

### **Come utilizzare i formati numerici incorporati**

Aspose.Cells offre alcuni formati numerici incorporati per configurare i formati di visualizzazione dei numeri e delle date. Questi formati numerici incorporati possono essere applicati utilizzando la proprietà [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/) dell'oggetto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Tutti i formati numerici incorporati hanno valori numerici univoci. Gli sviluppatori possono assegnare qualsiasi valore numerico desiderato alla proprietà [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/) dell'oggetto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) per applicare il formato di visualizzazione. Questo approccio è veloce. I formati numerici incorporati supportati da Aspose.Cells sono elencati di seguito.

|**Valore**|**Tipo**|**Stringa di formato**|
| :- | :- | :- |
|0|General|General|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|#,##0|
|4|Decimal|#,##0.00|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Red]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Red]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|# ?/?|
|13|Fraction|# */*|
|14|Date|m/d/yyyy|
|15|Date|d-mmm-yy|
|16|Date|d-mmm|
|17|Date|mmm-yy|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|h:mm|
|21|Time|h:mm:ss|
|22|Time|m/d/yy h:mm|
|37|Currency|#,##0;-#,##0|
|38|Currency|#,##0;[Red]-#,##0|
|39|Currency|#,##0.00;-#,##0.00|
|40|Currency|#,##0.00;[Red]-#,##0.00|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|##0.0E+00|
|49|Text|@|

```c++
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::time_t now = std::time(nullptr);
    double excelDate = static_cast<double>(now) / 86400.0 + 25569.0;
    worksheet.GetCells().Get(u"A1").PutValue(excelDate);

    Style style = worksheet.GetCells().Get(u"A1").GetStyle();
    style.SetNumber(15);
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    worksheet.GetCells().Get(u"A2").PutValue(20);
    style = worksheet.GetCells().Get(u"A2").GetStyle();
    style.SetNumber(9);
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    worksheet.GetCells().Get(u"A3").PutValue(2546);
    style = worksheet.GetCells().Get(u"A3").GetStyle();
    style.SetNumber(6);
    worksheet.GetCells().Get(u"A3").SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Come utilizzare i formati numerici personalizzati**

Per definire la propria stringa di formato personalizzata per impostare il formato di visualizzazione, utilizzare la proprietà [**Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/) dell'oggetto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Questo approccio non è veloce come l'uso dei formati preimpostati, ma è più flessibile.

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    auto now = std::chrono::system_clock::now();
    auto duration = now.time_since_epoch();
    auto hours = std::chrono::duration_cast<std::chrono::hours>(duration).count();
    double excelDate = hours / 24.0 + 25569.0;
    worksheet.GetCells().Get(u"A1").PutValue(excelDate);

    Style style = worksheet.GetCells().Get(u"A1").GetStyle();
    style.SetCustom(u"d-mmm-yy");
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    worksheet.GetCells().Get(u"A2").PutValue(20);
    style = worksheet.GetCells().Get(u"A2").GetStyle();
    style.SetCustom(u"0.0%");
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    worksheet.GetCells().Get(u"A3").PutValue(2546);
    style = worksheet.GetCells().Get(u"A3").GetStyle();
    style.SetCustom(u"£#,##0;[Red]$-#,##0");
    worksheet.GetCells().Get(u"A3").SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Se si utilizza la proprietà [**Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/) per impostare il formato numerico, qualsiasi formato precedente impostato utilizzando la proprietà [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/) viene sovrascritto e viceversa.

{{% /alert %}}

## **Argomenti avanzati**
- [Verificare il formato numerico personalizzato quando si imposta Style.Custom Property](/cells/it/cpp/check-custom-number-format-when-setting-style-custom-property/)
- [Elenco dei formati numerici supportati](/cells/it/cpp/list-of-supported-number-formats/)
- [Render Personalizzare data formato modello g e ge mm dd](/cells/it/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Specificare Personalizzare numerico Decimale e Gruppo Separatori per Cartella di lavoro](/cells/it/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Specifica di formattazione pattern personalizzato DBNum](/cells/it/cpp/specifying-dbnum-custom-pattern-formatting/)
{{< app/cells/assistant language="cpp" >}}
