---
title: Replace tag with text in a textbox inside the Worksheet with C++
linktitle: Replace tag with text in a textbox inside the Worksheet
type: docs
weight: 1100
url: /cpp/replace-tag-with-text-in-a-textbox-inside-the-worksheet/
description: Learn how to replace tags with text in a textbox inside a worksheet using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**
Text boxes can have tags which can be replaced with some text at run time to configure them according to the requirement. Tags can be some labels enclosed in angle brackets '<' and '>'. There can be multiple tags within a single textbox.

## **Sample Code**
Following sample code replaces tags TAG_1 and TAG_2 with some text say 'ys' and '1'. Sample file for testing below code can be downloaded from the following link:

[sampleReplaceTagWithText.xlsx](79527942.xlsx)

```c++
c++
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

void sheetReplace(Workbook& wb, const U16String& tag, const U16String& replace) {
    wb.Replace(tag, replace);
}

std::vector<U16String> SplitU16String(const U16String& str, char16_t delimiter) {
    std::vector<U16String> parts;
    int start = 0;
    int length = str.GetLength();
    for (int i = 0; i < length; ++i) {
        if (str[i] == delimiter) {
            parts.push_back(str.Substring(start, i - start));
            start = i + 1;
        }
    }
    parts.push_back(str.Substring(start));
    return parts;
}

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"sampleReplaceTagWithText.xlsx";
    U16String outputFilePath = outDir + u"outputReplaceTagWithText.pdf";

    Workbook wb(inputFilePath);

    U16String tag(u"TAG_2$TAG_1");
    U16String replace(u"1$ys");

    std::vector<U16String> tagParts = SplitU16String(tag, u'$');
    std::vector<U16String> replaceParts = SplitU16String(replace, u'$');

    for (size_t i = 0; i < tagParts.size(); ++i) {
        sheetReplace(wb, U16String(u"<") + tagParts[i] + U16String(u">"), replaceParts[i]);
    }

    PdfSaveOptions opts;
    wb.Save(outputFilePath, opts);

    std::cout << "Tags replaced and PDF saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

U16String ReplaceString(const U16String& input, const U16String& find, const U16String& replace) {
    std::u16string s = input.ToUtf16String();
    std::u16string f = find.ToUtf16String();
    std::u16string r = replace.ToUtf16String();

    size_t pos = 0;
    while ((pos = s.find(f, pos)) != std::u16string::npos) {
        s.replace(pos, f.length(), r);
        pos += r.length();
    }
    return U16String::FromUtf16(s.c_str());
}

void sheetReplace(Workbook& workbook, const U16String& sFind, const U16String& sReplace) {
    U16String finding = sFind;

    WorksheetCollection sheets = workbook.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); ++i) {
        Worksheet sheet = sheets.Get(i);
        sheet.Replace(finding, sReplace);

        for (int j = 0; j < 3; ++j) {
            HeaderFooterSectionType section = static_cast<HeaderFooterSectionType>(j);
            U16String header = sheet.GetPageSetup().GetHeader(section);
            if (!header.IsEmpty()) {
                U16String newHeader = ReplaceString(header, finding, sReplace);
                sheet.GetPageSetup().SetHeader(section, newHeader);
            }

            U16String footer = sheet.GetPageSetup().GetFooter(section);
            if (!footer.IsEmpty()) {
                U16String newFooter = ReplaceString(footer, finding, sReplace);
                sheet.GetPageSetup().SetFooter(section, newFooter);
            }
        }
    }

    for (int i = 0; i < sheets.GetCount(); ++i) {
        Worksheet sheet = sheets.Get(i);
        U16String modifiedFind = ReplaceString(sFind, u"<", u"&lt;");
        modifiedFind = ReplaceString(modifiedFind, u">", u"&gt;");

        TextBoxCollection textBoxes = sheet.GetTextBoxes();
        for (int j = 0; j < textBoxes.GetCount(); ++j) {
            TextBox mytextbox = textBoxes.Get(j);
            U16String htmlText = mytextbox.GetHtmlText();
            if (!htmlText.IsEmpty() && htmlText.IndexOf(modifiedFind) >= 0) {
                U16String newHtmlText = ReplaceString(htmlText, modifiedFind, sReplace);
                mytextbox.SetHtmlText(newHtmlText);
            }
        }
    }
}
```