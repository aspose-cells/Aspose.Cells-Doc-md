---
title: C++ ile Pivot Tablo için Küreselleşme Ayarlarını Özelleştir
linktitle: Pivot Tablo için Küreselleştirme Ayarlarını Özelleştir
type: docs
weight: 50
url: /tr/cpp/customize-globalization-settings-for-pivot-table/
description: Aspose.Cells for C++ kullanarak Pivot Tablo küreselleştirme ayarlarını nasıl özelleştireceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Bazen, ihtiyaçlarınıza göre *Pivot Toplam, Alt Toplam, Genel Toplam, Tüm Öğeler, Çoklu Öğeler, Sütun Etiketleri, Satır Etiketleri, Boş Değerler* metnini özelleştirmek istersiniz. Aspose.Cells for C++, bu tür durumlarla başa çıkmak için Pivot Tablo'nun küreselleşme ayarlarını özelleştirmenize olanak tanır. Ayrıca bu özelliği kullanarak etiketleri Arapça, Hintçe, Lehçe gibi diğer dillere de değiştirebilirsiniz.

## **Pivot Tablo için Küreselleştirme Ayarlarını Özelleştir**

Aşağıdaki örnek kod, C++ kullanarak Pivot Tablo'nun küreselleşme ayarlarını nasıl özelleştireceğinizi açıklar. [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.settings/pivotglobalizationsettings/) temel sınıfından türetilmiş *CustomPivotTableGlobalizationSettings* adlı bir sınıf oluşturur ve tüm gerekli yöntemleri geçersiz kılar. Bu yöntemler, çeşitli Pivot Tablo öğeleri için özelleştirilmiş metin döner. Kod daha sonra bu uygulamayı [**WorkbookSettings.GetPivotSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getpivotsettings/) özelliğine atar. Örnek, [kaynak Excel dosyasını](40468488.xlsx) yükler, pivot verisini yeniler ve [çıkış PDF'si](40468487.pdf) olarak kaydeder. Aşağıdaki ekran görüntüsü, çıktıdaki özelleştirilmiş etiketleri gösterir.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomPivotTableGlobalizationSettings : public PivotGlobalizationSettings {
public:
    virtual U16String GetTextOfTotal() override {
        std::cout << "---------GetPivotTotalName-------------" << std::endl;
        return u"AsposeGetPivotTotalName";
    }

    virtual U16String GetTextOfGrandTotal() override {
        std::cout << "---------GetPivotGrandTotalName-------------" << std::endl;
        return u"AsposeGetPivotGrandTotalName";
    }

    virtual U16String GetTextOfMultipleItems() override {
        std::cout << "---------GetMultipleItemsName-------------" << std::endl;
        return u"AsposeGetMultipleItemsName";
    }

    virtual U16String GetTextOfAll() override {
        std::cout << "---------GetAllName-------------" << std::endl;
        return u"AsposeGetAllName";
    }

    virtual U16String GetTextOfColumnLabels() override {
        std::cout << "---------GetColumnLabelsOfPivotTable-------------" << std::endl;
        return u"AsposeGetColumnLabelsOfPivotTable";
    }

    virtual U16String GetTextOfRowLabels() override {
        std::cout << "---------GetRowLabelsNameOfPivotTable-------------" << std::endl;
        return u"AsposeGetRowLabelsNameOfPivotTable";
    }

    virtual U16String GetTextOfEmptyData() override {
        std::cout << "---------GetEmptyDataName-------------" << std::endl;
        return u"(blank)AsposeGetEmptyDataName";
    }

    virtual U16String GetTextOfSubTotal(PivotFieldSubtotalType subTotalType) override {
        std::cout << "---------GetSubTotalName-------------" << std::endl;

        switch(subTotalType) {
            case PivotFieldSubtotalType::Sum:
                return u"AsposeSum";
            case PivotFieldSubtotalType::Count:
                return u"AsposeCount";
            case PivotFieldSubtotalType::Average:
                return u"AsposeAverage";
            case PivotFieldSubtotalType::Max:
                return u"AsposeMax";
            case PivotFieldSubtotalType::Min:
                return u"AsposeMin";
            case PivotFieldSubtotalType::Product:
                return u"AsposeProduct";
            case PivotFieldSubtotalType::CountNums:
                return u"AsposeCount";
            case PivotFieldSubtotalType::Stdev:
                return u"AsposeStdDev";
            case PivotFieldSubtotalType::Stdevp:
                return u"AsposeStdDevp";
            case PivotFieldSubtotalType::Var:
                return u"AsposeVar";
            case PivotFieldSubtotalType::Varp:
                return u"AsposeVarp";
            default:
                return u"AsposeSubTotalName";
        }
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook wb(srcDir + u"samplePivotTableGlobalizationSettings.xlsx");

    CustomPivotTableGlobalizationSettings customSettings;
    wb.GetSettings().GetGlobalizationSettings()->SetPivotSettings(&customSettings);

    wb.GetWorksheets().Get(0).SetIsVisible(false);

    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);

    pt.SetRefreshDataFlag(true);
    pt.RefreshData();
    pt.CalculateData();
    pt.SetRefreshDataFlag(false);

    PdfSaveOptions options;
    options.SetOnePagePerSheet(true);

    wb.Save(outDir + u"outputPivotTableGlobalizationSettings.pdf", options);

    std::cout << "Pivot table globalization settings applied successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
