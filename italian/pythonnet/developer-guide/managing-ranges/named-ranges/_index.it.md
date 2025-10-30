---
title: Creare Intervalli Nominati a Livello di Cartella e di Foglio
linktitle: Intervallo Nominato
type: docs
weight: 40
url: /it/python-net/create-workbook-and-worksheet-scoped-named-ranges/
description: Questo articolo mostra come creare intervalli nominati a livello di cartella e di foglio utilizzando l API Aspose.Cells for Python via .NET.
keywords: Libreria Excel Python, creare intervalli nominati a livello di cartella e di foglio con Python, aggiungere un intervallo nominato con ambito di cartella, aggiungere un intervallo nominato con ambito di foglio.
---

{{% alert color="primary" %}} 

Microsoft Excel consente agli utenti di definire intervalli nominati con due ambiti diversi: cartella di lavoro (noto anche come ambito globale) e foglio di lavoro.

- I nomi definiti con un ambito a livello di cartella di lavoro possono essere accessibili da qualsiasi foglio di calcolo all'interno di quella cartella di lavoro semplicemente usando il suo nome.
- I nomi definiti con ambito a livello di foglio di lavoro sono accessibili con il riferimento al foglio di lavoro particolare in cui sono stati creati.

Aspose.Cells per Python via .NET fornisce la stessa funzionalità di Microsoft Excel per l'aggiunta di nomi definiti con ambito a livello di cartella di lavoro e di foglio di lavoro. Quando si crea un nome definito a livello di foglio di lavoro, il riferimento al foglio di lavoro dovrebbe essere usato nel nome definito per specificarlo come un nome definito con ambito a livello di foglio di lavoro.


{{% /alert %}} 
## **Come Aggiungere un Nome Definito con Ambito a Livello di Cartella di Lavoro**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.py" >}}
## **Come Aggiungere un Nome Definito con Ambito a Livello del Foglio di Lavoro**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-WorkbookScopedNamedRanges-WorksheetNamedRange-1.py" >}}

## **Argomenti avanzati**
- [Crea accesso e copia intervalli con nome](/cells/it/python-net/create-access-and-copy-named-ranges/)
- [Formattare e modificare intervalli con nome](/cells/it/python-net/format-and-modify-named-ranges/)
- [Ottieni Intervallo con Link Esterni](/cells/it/python-net/get-range-with-external-links/)
- [Implementazione degli Intervallo Non Sequenziali](/cells/it/python-net/implementing-non-sequential-ranges/)
{{< app/cells/assistant language="python-net" >}}
