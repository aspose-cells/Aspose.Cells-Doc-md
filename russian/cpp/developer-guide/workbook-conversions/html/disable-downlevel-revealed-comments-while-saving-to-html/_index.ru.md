---
title: Отключить объяснительные комментарии следующего уровня при сохранении в HTML с помощью C++
linktitle: Отключить объяснительные комментарии следующего уровня
type: docs
weight: 20
url: /ru/cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Устранить объяснительные комментарии следующего уровня при сохранении файлов Excel в HTML с помощью Aspose.Cells и C++.
---

## **Возможные сценарии использования**

При сохранении файла Excel в HTML Aspose.Cells отображает условные комментарии следующего уровня. Эти условные комментарии в основном актуальны для старых версий Internet Explorer и не имеют значения для современных браузеров. Подробнее о них можно прочитать по следующей ссылке.

- [Условный комментарий - условный комментарий с раскрытием](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells позволяет устранить эти комментарии следующего уровня, установив свойство [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/) в значение **true**.

## **Отключить отображение устаревших комментариев при сохранении в HTML**

Следующий пример кода показывает использование свойства [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/). На снимке экрана видно, как влияет это свойство, когда оно не установлено в значение true. Для ознакомления скачайте [пример файла Excel](50528257.xlsx), использованный в этом коде, и [сгенерированный HTML](50528258.zip) для просмотра.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample workbook
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(sourceDir + u"sampleDisableDownlevelRevealedComments.xlsx");

    // Disable DisableDownlevelRevealedComments
    HtmlSaveOptions opts;
    opts.SetDisableDownlevelRevealedComments(true);

    // Save the workbook in html
    wb.Save(outputDir + u"outputDisableDownlevelRevealedComments_true.html", opts);

    std::cout << "Workbook saved successfully with DisableDownlevelRevealedComments enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
