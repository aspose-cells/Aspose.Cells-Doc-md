---
title: Impostazione Formule  Avviso per gli Utenti Non Anglofoni
type: docs
weight: 10
url: /it/python-net/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET supporta la maggior parte delle formule/funzioni presenti in Microsoft Excel. Gli sviluppatori possono usare queste formule sia con l'API che con [designer spreadsheets](/cells/it/net/what-is-a-designer-spreadsheet/). Aspose.Cells for Python via .NET supporta un grande insieme di formule matematiche, stringa, Boolean, data/ora, statistica, database, ricerche e riferimenti. Le formule devono essere specificate usando lo stile inglese (USA).

{{% /alert %}} 

## **Avviso per gli Utenti Non Anglofoni**
Ci sono due consigli che gli utenti non anglofoni devono seguire quando creano formule con Aspose.Cells for Python via .NET:

1. Le formule devono essere inserite in inglese. Per esempio, utilizzare l'inglese "=SUM()" e non il tedesco "=SUMME()".
1. Usa sempre una virgola (,) per delimitare i parametri della funzione. Per alcune opzioni di lingua o impostazioni, il delimitatore dei parametri della funzione è un punto e virgola, ma Aspose.Cells for Python via .NET utilizza lo stile inglese virgola. Ad esempio, usa "=SE (C5=0;0;C3/C4)" non "=SE(C5=0;0;C3/C4)"

{{< app/cells/assistant language="python-net" >}}
