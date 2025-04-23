---
title: Creare Intervalli Nominati a Livello di Cartella e di Foglio
linktitle: Intervallo Nominato
type: docs
weight: 40
url: /it/net/create-workbook-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}} 

Microsoft Excel consente agli utenti di definire intervalli nominati con due ambiti diversi: cartella di lavoro (noto anche come ambito globale) e foglio di lavoro.

- I nomi definiti con un ambito a livello di cartella di lavoro possono essere accessibili da qualsiasi foglio di calcolo all'interno di quella cartella di lavoro semplicemente usando il suo nome.
- I nomi definiti con ambito a livello di foglio di lavoro sono accessibili con il riferimento al foglio di lavoro particolare in cui sono stati creati.

Aspose.Cells fornisce la stessa funzionalità di Microsoft Excel per l'aggiunta di intervalli con nome a livello di cartella di lavoro e di foglio di lavoro. Quando si crea un intervallo con nome a livello di foglio di lavoro, deve essere utilizzato il riferimento del foglio di lavoro nell'intervallo con nome per specificarlo come intervallo con nome a livello di foglio di lavoro.

{{% /alert %}} 
## **Aggiunta di un intervallo con nome a livello di cartella di lavoro**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.cs" >}}
## **Aggiunta di un intervallo con nome a livello di foglio di lavoro**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-WorksheetNamedRange-1.cs" >}}

## **Argomenti avanzati**
- [Crea accesso e copia intervalli con nome](/cells/it/net/create-access-and-copy-named-ranges/)
- [Formattare e modificare intervalli con nome](/cells/it/net/format-and-modify-named-ranges/)
- [Ottieni Intervallo con Link Esterni](/cells/it/net/get-range-with-external-links/)
- [Implementazione degli Intervallo Non Sequenziali](/cells/it/net/implementing-non-sequential-ranges/)
{{< app/cells/assistant language="csharp" >}}
