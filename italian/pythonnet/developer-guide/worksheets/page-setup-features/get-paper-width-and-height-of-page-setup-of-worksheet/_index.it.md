---
title: Ottieni larghezza e altezza della carta della configurazione della pagina del foglio di lavoro
type: docs
weight: 50
url: /it/python-net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: In questo articolo scoprirai come ottenere larghezza e altezza del foglio Excel utilizzando il codice Python in modo programmato con Aspose.Cells per Python via .NET API o Libreria.
keywords: Libreria Python Excel, larghezza formato carta setup pagina excel, altezza formato carta setup pagina excel in Python.
---

## **Possibili Scenari di Utilizzo**

A volte è necessario conoscere la larghezza e l'altezza della dimensione della carta come è stata impostata nella configurazione della pagina del foglio di lavoro. Si prega di utilizzare le proprietà [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) e [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height) a questo scopo.

## **Ottenere larghezza e altezza della pagina di configurazione del foglio di lavoro**

Il codice di esempio seguente spiega l'utilizzo delle proprietà [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) e [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height). Prima cambia il formato carta in *A2* e successivamente trova la larghezza e l'altezza del foglio, poi lo cambia in *A3*, *A4*, *Letter* e rispettivamente trova la larghezza e l'altezza del foglio.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-GetPageDimensions.py" >}}

### **Output della console**

Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
