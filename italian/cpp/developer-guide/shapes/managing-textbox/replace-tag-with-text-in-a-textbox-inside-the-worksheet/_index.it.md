---
title: Sostituisci tag con testo in una TextBox all’interno del Foglio di Lavoro con C++
linktitle: Sostituisci il tag con il testo in una casella di testo all interno del foglio di lavoro
type: docs
weight: 1100
url: /it/cpp/replace-tag-with-text-in-a-textbox-inside-the-worksheet/
description: Sostituisci i tag nei textbox del foglio di lavoro programmaticamente usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**
Text boxes can have tags which can be replaced with some text at run time to configure them according to the requirement. Tags can be some labels enclosed in angle brackets '<' and '>'. There can be multiple tags within a single textbox.

## **Codice di Esempio**
Il codice di esempio seguente sostituisce i tag TAG_1 e TAG_2 con del testo come 'ys' e '1'. È possibile scaricare il file di esempio per testare il codice dal seguente link:

[sampleReplaceTagWithText.xlsx](79527942.xlsx)

```c++
#include <Aspose.Cells.h>
#include <regex>
#include <vector>
#include <string>

using namespace Aspose::Cells;

U16String Replace(const U16String& ustr, const std::u16string& from, const std::u16string& to, bool replaceAll) {
    std::u16string str(ustr.GetData());
    if (!from.empty())
    {
        size_t start_pos = 0;
        while ((start_pos = str.find(from, start_pos)) != std::u16string::npos) {
            str.replace(start_pos, from.length(), to);
            if (!replaceAll)
            {
                break;
            }
            start_pos += to.length();
        }
    }
    return U16String(str.c_str());
}

std::vector<U16String> Split(const U16String& str, const char16_t delim)
{
    std::u16string u16str(str.GetData());
    std::vector<U16String> result;

    size_t start = 0;
    size_t end = u16str.find(delim);

    while (end != std::u16string::npos)
    {
        std::u16string substr = u16str.substr(start, end - start);
        result.push_back(U16String(substr.c_str()));
        start = end + 1;
        end = u16str.find(delim, start);
    }

    // Add the last part
    std::u16string substr = u16str.substr(start);
    result.push_back(U16String(substr.c_str()));

    return result;
}

void sheetReplace(Workbook& workbook, U16String sFind, const U16String& sReplace)
{
    U16String finding = sFind;

    WorksheetCollection sheets = workbook.GetWorksheets();
    int sheetCount = sheets.GetCount();

    // Replace text in cells and headers/footers
    for (int i = 0; i < sheetCount; ++i)
    {
        Worksheet sheet = sheets.Get(i);
        sheet.Replace(finding, sReplace);

        PageSetup pageSetup = sheet.GetPageSetup();
        for (int j = 0; j < 3; ++j)
        {
            U16String header = pageSetup.GetHeader(j);
            if (!header.IsEmpty())
            {
                header = Replace(header, std::u16string(finding.GetData()), std::u16string(sReplace.GetData()), true);
                pageSetup.SetHeader(j, header);
            }

            U16String footer = pageSetup.GetFooter(j);
            if (!footer.IsEmpty())
            {
                footer = Replace(footer, std::u16string(finding.GetData()), std::u16string(sReplace.GetData()), true);
                pageSetup.SetFooter(j, footer);
            }
        }
    }

    // Replace text in textboxes with HTML entities
    for (int i = 0; i < sheetCount; ++i)
    {
        Worksheet sheet = sheets.Get(i);

        U16String modifiedFind = sFind;
        modifiedFind = Replace(modifiedFind, std::u16string(u"<"), std::u16string(u"&lt;"), true);
        modifiedFind = Replace(modifiedFind, std::u16string(u">"), std::u16string(u"&gt;"), true);

        TextBoxCollection textBoxes = sheet.GetTextBoxes();
        int textBoxCount = textBoxes.GetCount();
        for (int j = 0; j < textBoxCount; ++j)
        {
            TextBox textBox = textBoxes.Get(j);
            U16String htmlText = textBox.GetHtmlText();
            int32_t findPos = htmlText.IndexOf(modifiedFind);
            if (!htmlText.IsEmpty() && findPos >= 0)
            {
                htmlText = Replace(htmlText, std::u16string(modifiedFind.GetData()), std::u16string(sReplace.GetData()), true);
                textBox.SetHtmlText(htmlText);
            }
        }
    }
}

int main() {
    Aspose::Cells::Startup();

    Workbook wb(U16String(u"G:\\sampleReplaceTagWithText.xlsx"));

    U16String tag(u"TAG_2$TAG_1");
    U16String replace(u"1$ys");

    std::vector<U16String> tagParts = Split(tag, u'$');
    std::vector<U16String> replaceParts = Split(replace, u'$');

    for (size_t i = 0; i < tagParts.size() && i < replaceParts.size(); i++)
    {
        U16String findStr = U16String(u"<") + tagParts[i] + U16String(u">");
        sheetReplace(wb, findStr, replaceParts[i]);
    }

    PdfSaveOptions opts;
    wb.Save("outputReplaceTagWithText.pdf", opts);

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
