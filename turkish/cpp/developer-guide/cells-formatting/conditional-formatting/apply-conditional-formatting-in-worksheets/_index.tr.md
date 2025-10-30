---
title: Çalışma Sayfalarında Koşullu Biçimlendirme Uygula C++ ile
linktitle: Koşullu Biçimlendirmeyi Uygula
description: C++ dilinde Aspose.Cells kütüphanesini kullanarak çalışma sayfalarında koşullu biçimlendirme nasıl uygulanır. Bu kriterleri ayarlayarak hücrelerin görünümünü ve görünüşünü daha iyi kontrol edebilirsiniz.
keywords: Aspose.Cells, Koşullu Biçimlendirme, C++, Çalışma Sayfası, Biçimlendirme
type: docs
weight: 130
url: /tr/cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Bu makale, bir çalışma sayfasındaki hücre aralığına koşullu biçimlendirme eklemenin detaylı bir anlayışını sağlamak amacıyla tasarlanmıştır.

Koşullu biçimlendirme, Microsoft Excel'de gelişmiş bir özelliktir ve bir hücrenin değerine veya bir formülün değerine bağlı olarak biçimlendirme uygulamanıza olanak tanır. Örneğin, bir hücrenin arka planı, negatif bir değeri vurgulamak için kırmızı olabilir veya pozitif bir değer için metin rengi yeşil olabilir. Hücrenin değeri biçim koşulunu karşıladığında, biçim uygulanır. Hücrenin değeri biçim koşulunu karşılamadığında, hücrenin varsayılan biçimlendirmesi kullanılır.

Microsoft Office Automation ile koşullu biçimlendirme uygulamak mümkündür ancak bunun dezavantajları vardır. Örneğin, güvenlik, istikrar, ölçeklenebilirlik ve hız gibi çeşitli nedenler ve sorunlar bulunmaktadır. Başka bir çözüm bulma ana nedeni, Microsoft'un kendisinin yazılım çözümleri için Office Automation'a kesinlikle karşı çıkmasıdır.

Bu makale, Aspose.Cells API kullanarak birkaç basit kod satırıyla hücrelere koşullu biçimlendirme eklemeyi göstermektedir.

{{% /alert %}}

## **Hücre Değerine Bağlı Olarak Koşullu Biçimlendirme Uygulamak İçin Aspose.Cells Kullanma**

1. **Aspose.Cells'ı İndirin ve Kurun**.
   1. Aspose.Cells for C++ numaralı dosyayı indirin.
1. Geliştirme bilgisayarınıza kurun.
   Kurulduğunda, tüm Aspose bileşenleri değerlendirme modunda çalışır. Değerlendirme modunun süresiz bir sınırlaması yoktur ve yalnızca üretilen belgelere filigran enjekte eder.
1. **Bir proje oluşturun.**
   Geliştirme ortamınızı başlatın ve yeni bir konsol uygulaması oluşturun.
1. **Referanslar Ekleyin**.
   Projeye Aspose.Cells'a bir referans ekleyin, örneğin ….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll gibi bir referans ekleyin
1. **Hücre değerine dayalı koşullu biçimlendirme uygula**.
   Aşağıda, görevi yerine getirmek için kullanılan kod yer almaktadır. Bu, hücre üzerinde koşullu biçimlendirme uygular.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiating a Workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the FormatConditionCollection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(0, 0, 0, 0);

    // Add the cell area to the format condition collection
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Sets the background color
    fc.GetStyle().SetBackgroundColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Yukarıdaki kod yürütüldüğünde, çıktı dosyasının (output.xls) ilk çalışma sayfasındaki “A1” hücresine koşullu biçimlendirme uygulanır. A1 hücresine uygulanan koşullu biçimlendirme, hücre değere bağlıdır. A1 hücresinin değeri 50 ile 100 arasında ise, koşullu biçimlendirme nedeniyle arka plan rengi kırmızı olur.

## **Aspose.Cells Kullanarak Formül Değerine Bağlı Olarak Koşullu Biçimlendirme Uygulama**

1. **Formüle bağlı koşullu biçimlendirme uygulama (Kod Parçası)**
   Aşağıda verilen kod, görevi gerçekleştirmek için kullanılan koddur. B3'e koşullu biçimlendirme uygular.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the conditional formatting collection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(2, 1, 2, 1);

    // Add the area to the conditional formatting
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::Expression);

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Set the formula for the condition
    fc.SetFormula1(u"=IF(SUM(B1:B2)>100,TRUE,FALSE)");

    // Set the background color
    Style style = fc.GetStyle();
    style.SetBackgroundColor(Color::Red());
    fc.SetStyle(style);

    // Set the formula for cell B3
    sheet.GetCells().Get(u"B3").SetFormula(u"=SUM(B1:B2)");

    // Set the value for cell C4
    sheet.GetCells().Get(u"C4").PutValue(u"If Sum of B1:B2 is greater than 100, B3 will have RED background");

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Yukarıdaki kod yürütüldüğünde, çıktı dosyasının (output.xls) ilk çalışma sayfasındaki “B3” hücresine koşullu biçimlendirme uygulanır. Uygulanan koşullu biçimlendirme, B3 hücresinin B1 ve B2 toplamı olarak hesaplanan değere bağlıdır.
{{< app/cells/assistant language="cpp" >}}
