---
title: Использование только DLL
type: docs
weight: 20
url: /ru/reportingservices/using-dll-only/
---
## Как установить Aspose.Cells for Reporting Services, используя только DLL:

-  Посетите Aspose.Cells for Reporting Services[страница загрузки](https://downloads.aspose.com/cells/reportingservices) и скачать**Aspose.Cells for Reporting Services (почтовый индекс)** архив, содержащий последнюю версию компонента и установленную документацию.
 - Существует 7 видов версий Aspose.Cells.ReprotingServices.dll в Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. Они поддерживают различные продукты сервера отчетов Microsoft.
 - Aspose.Cells.ReportingServices.dll в папке SSRS2005 поддерживает службы отчетов SQL Server 2005 Microsoft.
 - Aspose.Cells.ReportingServices.dll в папке SSRS2008 поддерживает службы отчетов SQL Server 2008 Microsoft.
 - Aspose.Cells.ReportingServices.dll в папке SSRS2008R2 поддерживает службы отчетов Microsoft SQL Server 2008R2/2012/2014.
 - Aspose.Cells.ReportingServices.dll в папке SSRS2016 поддерживает службы отчетов Microsoft SQL Server 2016/2017/2019.
   
- Распаковать архив в директорию на жестком диске.

- Установите Aspose.Cells for Reporting Services Дизайнер отчетов:
 - Регистр**Aspose.Cells.ReportingServices.Client.dll** с помощью утилиты Regasm.exe.
 - Добавить надстройку Aspose.Cells for Reporting Services в Excel.
   
- Установите Aspose.Cells for Reporting Services для Microsoft SQL Server Reporting Services компонент служб:
 - Положите**Aspose.Cells.ReportingServices.dll** в папку установки ${Microsoft SQL Server Reporting Services}\ReportServer\bin.
 - Добавлено Aspose.Cells for Reporting Services расширений рендерера:
 - Открытым**${Microsoft Папка установки SQL Server Reporting Services}\ReportServer\rsreportserver.config**
 - Добавьте следующие строки в<Render>……</Render> элемент:
{{< highlight "xml" >}}

 <Render>

...

<!--Start here.-->

<Extension Name="ACXLS" Type="Aspose.Cells.ReportingServices.XlsRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXLSX" Type="Aspose.Cells.ReportingServices.Excel2007XlsxRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXLSX(Data Only)" Type="Aspose.Cells.ReportingServices.Excel2007SimpleXlsxRenderer,Aspose.Cells.ReportingServices"/>

<Extension Name="ACXLSB" Type="Aspose.Cells.ReportingServices.XlsbRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXLSM" Type="Aspose.Cells.ReportingServices.Excel2007XlsmRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXML" Type="Aspose.Cells.ReportingServices.SpreadsheetMLRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACHTML" Type="Aspose.Cells.ReportingServices.HtmlRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACCSV" Type="Aspose.Cells.ReportingServices.CSVRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACODS" Type="Aspose.Cells.ReportingServices.ODSRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACTXT" Type="Aspose.Cells.ReportingServices.TabDelimitedRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXPS" Type="Aspose.Cells.ReportingServices.XpsRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACMD" Type="Aspose.Cells.ReportingServices.MarkdownRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACTIFF" Type="Aspose.Cells.ReportingServices.TIFFRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACPDF" Type="Aspose.Cells.ReportingServices.PDFRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACPNG" Type="Aspose.Cells.ReportingServices.PNGRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACJPG" Type="Aspose.Cells.ReportingServices.JPGRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACEMF" Type="Aspose.Cells.ReportingServices.EMFRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACDIF" Type="Aspose.Cells.ReportingServices.DifRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACSVG" Type="Aspose.Cells.ReportingServices.SvgRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACJSON" Type="Aspose.Cells.ReportingServices.JsonRenderer,Aspose.Cells.ReportingServices" />
<!--End here.-->

</Render>

{{< /highlight >}}
 - Добавить Aspose.Cells for Reporting Services разрешения на выполнение:
 - Открытым**${Microsoft Папка установки SQL Server Reporting Services}\ReportServer\rssrvpolicy.config** и
 - Добавьте следующее как последний элемент во втором к внешнему<CodeGroup> элемент (который должен быть<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. "> ): 

{{< highlight "xml" >}}

 <CodeGroup>

...

<CodeGroup>

...

<!--Start here.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust" Name="Aspose.Cells_for_Reporting_Services" Description="This code group grants full trust to the Aspose.Cells for Reporting Services assembly.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001002780c08eaa89aedfb00b1b96137cca3e15f32826e0e4fd1da3c98d1e3968a03a019aa7b7228b151f6e5dae4dcb00f98479770f507626b04e786e5e93ec3757c1cc4ed1ac4b72c7649c4438e9d3a5f44d8b7522043686a2e8c2a495e04b917e0505d3201015c828e3c15afc8a46ab78293574b9e0475df68627bbabc5b564addd" />

</CodeGroup>

<!--End here.-->

</CodeGroup>

</CodeGroup>

{{< /highlight >}}

## Убедитесь, что Aspose.Cells for Reporting Services успешно установлен:
1. Откройте диспетчер отчетов и проверьте список доступных типов экспорта для отчета. (Запустите диспетчер отчетов, открыв браузер и введите URL-адрес диспетчера отчетов в адресную строку. (По умолчанию URL-адрес — http://<ComputerName>/Отчеты).
 1. Выберите один из отчетов на сервере и откройте**Выберите формат** список.
 Вы должны увидеть список форматов экспорта, предоставленный Aspose.Cells for Reporting Services.
 1. Выберите**XLS – Книга Excel через Aspose.Cells**.
 1. Нажмите**Экспорт**.
 Отчет формируется в выбранном формате.
 1. Отправьте его клиенту и откройте в соответствующем приложении. В этом случае отчет открывается в Microsoft Excel.

Поздравляем, вы успешно установили Aspose.Cells for Reporting Services и создали отчет в виде файла Excel Microsoft!


 Существует 7 видов версий Aspose.Cells.ReprotingServices.dll в Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. Они поддерживают различные продукты сервера отчетов Microsoft.