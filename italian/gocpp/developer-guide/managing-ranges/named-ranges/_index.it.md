---
title: Crea intervalli nominati con ambito di cartella di lavoro e di foglio di lavoro con Golang via C++
linktitle: Intervallo Nominato
type: docs
weight: 40
url: /it/go-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Impara a creare intervalli nominati con ambito di cartella di lavoro e di foglio di lavoro con Golang via C++ usando Aspose.Cells.
---

{{% alert color="primary" %}} 

Microsoft Excel consente agli utenti di definire intervalli nominati con due ambiti diversi: cartella di lavoro (noto anche come ambito globale) e foglio di lavoro.

- I nomi definiti con un ambito a livello di cartella di lavoro possono essere accessibili da qualsiasi foglio di calcolo all'interno di quella cartella di lavoro semplicemente usando il suo nome.
- I nomi definiti con ambito a livello di foglio di lavoro sono accessibili con il riferimento al foglio di lavoro particolare in cui sono stati creati.

Aspose.Cells fornisce la stessa funzionalità di Microsoft Excel per l'aggiunta di intervalli con nome a livello di cartella di lavoro e di foglio di lavoro. Quando si crea un intervallo con nome a livello di foglio di lavoro, deve essere utilizzato il riferimento del foglio di lavoro nell'intervallo con nome per specificarlo come intervallo con nome a livello di foglio di lavoro.

{{% /alert %}} 

## **Aggiunta di un intervallo con nome a livello di cartella di lavoro**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NamedRanges.go" >}}
## **Aggiunta di un intervallo con nome a livello di foglio di lavoro**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NamedRanges-1.go" >}}
## **Argomenti avanzati**
- [Crea accesso e copia intervalli con nome](/cells/it/cpp/create-access-and-copy-named-ranges/)
- [Formattare e modificare intervalli con nome](/cells/it/cpp/format-and-modify-named-ranges/)
- [Ottieni Intervallo con Link Esterni](/cells/it/cpp/get-range-with-external-links/)
- [Implementazione degli Intervallo Non Sequenziali](/cells/it/cpp/implementing-non-sequential-ranges/)

