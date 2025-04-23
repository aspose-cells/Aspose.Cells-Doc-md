---
title: Hämta HTML5 sträng från cell
type: docs
weight: 90
url: /sv/nodejs-cpp/get-html5-string-from-cell/
description: Lär dig hur du hämtar HTML5 sträng från cell via API et Aspose.Cells for Node.js via C++.
keywords: Hämta HTML5 sträng från cell Node.js via C++, Obtaining HTML5 sträng från cell Node.js via C++, Hantera HTML5 sträng för cell Node.js via C++
---

## **Möjliga användningsscenario**

Aspose.Cells returnerar HTML-strängen för cellen med hjälp av [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-)-metoden som tar emot en boolean-parameter. Om du skickar **false** som parameter, returnerar den vanlig HTML, men om du skickar **true**, returnerar den HTML5-sträng.

## **Hämta HTML5-sträng från cell**

Följande exempel skapar ett arbetsboksobjekt och lägger till lite text i cell A1 i det första kalkbladet. Sedan hämtar den den normala HTML och HTML5-sträng från cell A1 med [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-)-metoden och skriver ut dem i konsolen.

## **Exempelkod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-HtmlStringValue-GetHtml5String.js" >}}


## **Konsoloutput**

{{< highlight javascript >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
