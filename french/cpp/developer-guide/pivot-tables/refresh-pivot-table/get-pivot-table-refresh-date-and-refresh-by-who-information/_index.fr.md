---
title: Obtenir la date de mise à jour du tableau croisé dynamique et les informations sur la personne l’ayant actualisé avec C++
linktitle: Obtenir la date de mise à jour du tableau croisé dynamique et les informations sur la personne l’ayant actualisé
type: docs
weight: 100
url: /fr/cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Apprenez comment récupérer la date de mise à jour et les informations sur la personne l’ayant actualisé d’un classeur en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Aspose.Cells prend désormais en charge la récupération de la date de rafraîchissement et des informations sur qui a effectué le rafraîchissement à partir d'un classeur.

{{% /alert %}}

[**PivotTable.GetRefreshDate()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshdate/) renvoie la date à laquelle le rapport de tableau croisé dynamique a été rafraîchi pour la dernière fois. De même, la propriété [**PivotTable.GetRefreshedByWho()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshedbywho/) renvoie le nom de l'utilisateur qui a rafraîchi le rapport en dernier lieu. L'exemple suivant démontre cette fonctionnalité, et le fichier d'exemple peut être téléchargé à partir du lien suivant.

[SourcePivotTable.xlsx](77496335.xlsx)

**Code d'exemple**

```cpp
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

std::string Date_To_String(const Aspose::Cells::Date& date) {
    char buffer[100];
    snprintf(buffer, sizeof(buffer), "%04d-%02d-%02d %02d:%02d:%02d",
             date.year, date.month, date.day, date.hour, date.minute, date.second);
    return buffer;
}

std::string convert_u16_to_string(const char16_t* str) {
    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
    return converter.to_bytes(str);
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"sourcePivotTable.xlsx");

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    std::cout << "Pivot table refresh by who = " << convert_u16_to_string(pivotTable.GetRefreshedByWho().GetData()) << std::endl;

    std::cout << "Pivot table refresh date = " << Date_To_String(pivotTable.GetRefreshDate()) << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
