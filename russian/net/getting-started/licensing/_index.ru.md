---
title: Licensing
type: docs
weight: 120
url: /ru/net/licensing/
description: Aspose.Cells for .NET предоставляет различные планы для покупки или предлагает бесплатную пробную версию и 30-дневную временную лицензию для ознакомления с использованием Licensing и политик подписки в C#.
keywords: Apply License from Disk or Stream. Set License from Disk or Stream. Apply License in Aspose.Cells.
---
{{% alert color="primary" %}}

 Вы можете легко загрузить ознакомительную версию Aspose.Cells с[страница загрузки](https://www.nuget.org/packages/Aspose.Cells) @NuGet репозиторий. Ознакомительная версия предоставляет абсолютно те же возможности, что и лицензионная версия компонента. Более того, ознакомительная версия просто становится лицензированной, когда вы покупаете лицензию и добавляете пару строк кода для применения лицензии.

{{% /alert %}}

##  **Ограничения ознакомительной версии**

Ознакомительная версия продукта Aspose.Cells (без указания лицензии) обеспечивает полную функциональность продукта, но ограничена открытием 100 файлов в одной программе и дополнительным рабочим листом с оценочным водяным знаком.

Ограничения показаны ниже:

- **Количество открытых файлов** (Aspose.Cells)
 При запуске вашей программы вы можете открыть только 100 файлов Excel, используя библиотеку Aspose.Cells. Если ваше приложение превышает это число, будет выдано исключение.
- **Настройки файла конфигурации**(Aspose.Cells.GridWeb)
 Вы не можете повторно указать путь к скрипту, добавив следующие строки кода в раздел конфигурации (например, в файл web.config). Acw_client — это папка, содержащая файлы, и Aspose.Cells.GridWeb использует эту папку для управления своей внутренней конфигурацией. В ней есть файлы сценариев, файлы изображений и другие файлы для указания поведения GridWeb и установки других операций. Файл конфигурации используется для предотвращения использования элементом управления встроенных клиентских ресурсов (изображений, сценариев и т. д.), что полезно в некоторых случаях/сценариях. Более того, эти параметры конфигурации в файле web.config вступят в силу только с ЛИЦЕНЗИОННОЙ версией элемента управления.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Эти настройки могут быть обязательными в некоторых случаях/сценариях, если вы используете элемент управления Aspose.Cells.GridWeb на веб-сайтах файловой системы или в расширениях MS Ajax и т. д.

{{% /alert %}}

Более того, лист с оценочным водяным знаком всегда будет отображаться как активный лист в созданном файле Excel с использованием библиотеки Aspose.Cells. Только в лицензионной версии вы можете установить активный лист на другие листы. В выходном файле PDF или файле изображения с номером Aspose.Cells оценочный водяной знак будет вставлен в верхнюю часть документа/изображения. Вы также не можете скрыть предупреждение об авторских правах оценки (дополнительный рабочий лист) в элементе управления GridWeb, оно всегда будет добавлено. (в конце на вкладках листа) в элементе управления.

{{% alert color="primary" %}}

 Если вы хотите протестировать Aspose.Cells без ограничений ознакомительной версии, вы также можете запросить[Временная лицензия на 30 дней](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

##  **Как применить лицензию в компоненте Aspose.Cells**

Лицензия представляет собой обычный текстовый XML-файл, содержащий такие сведения, как название продукта, количество разработчиков, которым предоставлена лицензия, дата истечения срока подписки и т. д. Файл имеет цифровую подпись, поэтому не изменяйте его. Даже случайное добавление дополнительного разрыва строки в файл сделает его недействительным. Вам необходимо установить лицензию перед использованием Aspose.Cells, если вы хотите избежать ограничений ее оценки. Для каждого приложения (или процесса) лицензию требуется установить только один раз. Лицензию можно загрузить из файла, потока или встроенного ресурса.

Aspose.Cells пытается найти лицензию в следующих местах:

- Явный путь
- Папка, содержащая Aspose.Cells.dll.
- Папка, содержащая сборку с именем Aspose.Cells.dll.
- Папка, содержащая входную сборку (ваш .exe).
- Встроенный ресурс в сборке с именем Aspose.Cells.dll.

Существует два распространенных метода применения лицензии: из файла или потока или в виде встроенного ресурса.

###  **Как применить лицензию с диска или потока**

Самый простой способ установить лицензию — поместить файл лицензии в ту же папку, что и файл Aspose.Cells.dll, и указать только имя файла без пути.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

При вызове метода SetLicense имя лицензии должно совпадать с именем файла лицензии. Например, вы можете изменить имя файла лицензии на *Aspose.Cells.lic.xml**. Затем в своем коде вам следует использовать измененное имя лицензии (**Aspose.Cells.lic.xml**) для метода SetLicense.

{{% /alert %}}

Также есть возможность загрузить лицензию из потока.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **Как применить лимитную лицензию**

Aspose.Cells позволяет разработчикам применять дозированный ключ. Это новый механизм лицензирования. Новый механизм лицензирования будет использоваться наряду с существующим методом лицензирования. Те клиенты, которые хотят, чтобы им выставлялись счета на основе использования функций API, могут использовать дозированное лицензирование. Для получения более подробной информации см.[Измеренный Licensing Часто задаваемые вопросы](https://purchase.aspose.com/faqs/licensing/metered)раздел.

Новый класс[Измеренный](https://reference.aspose.com/cells/net/aspose.cells/metered)было введено применение дозированного ключа. Ниже приведен пример кода, демонстрирующий, как установить измеренный открытый и закрытый ключ.

{{< highlight "csharp" >}}

 //Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.SetMeteredKey("*************", "*************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

Console.WriteLine(workbook.IsLicensed);

//Get the Consumption quantity

decimal amountBefore = Metered.GetConsumptionQuantity();

Console.WriteLine(amountBefore);

Workbook workbook2 = new Workbook("e:\\test2\\Book1.xlsx");

workbook2.Save("e:\\test2\\out1.xlsx");

//Since uploading data is already running on another thread, so you might need to wait for some time (optional)

System.Threading.Thread.Sleep(10000);

//Get the Consumption quantity again which should be greater a bit

decimal amountAfter = Metered.GetConsumptionQuantity();

Console.WriteLine(amountAfter);

{{< /highlight >}}

###  **Как использовать встроенный ресурс**

Еще один удобный способ упаковать лицензию в приложение и гарантировать, что она не будет потеряна, — включить ее в качестве встроенного ресурса в одну из сборок, вызывающую Aspose.Cells. Чтобы включить файл лицензии в качестве встроенного ресурса, выполните следующие действия. :

1.  В Visual Studio .NET включите файл лицензии (.lic) в проект, выбрав его.**Добавить существующий элемент** из**Файл** меню.
1.  Выберите файл в обозревателе решений и установите**Действие сборки** к**Встроенный ресурс** в окне свойств

Для доступа к лицензии, встроенной в сборку (как внедренный ресурс), не требуется вызывать методы GetExecutingAssembly и GetManifestResourceStream класса System.Reflection.Assembly Microsoft .NET Framework. Все, что нужно сделать, — это просто добавить файл лицензии в качестве встроенного ресурса в ваш проект и передать имя файла лицензии в метод SetLicense.**Aspose.Cells.License** class автоматически найдет файл лицензии во встроенных ресурсах. Ознакомьтесь с приведенным ниже примером, чтобы понять этот метод установки лицензии (встроенной) в ваши приложения.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **Как установить лицензию в Aspose.Cells Grid Controls**

В Aspose.Cells Grid Suite лицензию можно загрузить из файла, потока или встроенного ресурса. Aspose.Cells.GridDesktop/Aspose.Cells.GridWeb пытается найти лицензию в следующих местах:

1. Явный путь
1. Папка, содержащая dll компонента (включена в Aspose.Cells.GridDesktop или Aspose.Cells.GridWeb).
1. Папка, содержащая сборку, вызывающую dll компонента (включена в Aspose.Cells.GridDesktop или Aspose.Cells.GridWeb).
1. Папка, содержащая входную сборку (ваш .exe).
1. Встроенный ресурс в сборке, вызывающий dll компонента (включенный в Aspose.Cells.GridDesktop или Aspose.Cells.GridWeb).

{{% alert color="primary" %}}

Если вы используете элемент управления Aspose.Cells.GridDesktop, то класс лицензии будет использоваться как Aspose.Cells.GridDesktop.License, но если вы используете элемент управления Aspose.Cells.GridWeb, то для установки лицензии будет использоваться класс Aspose.Cells.GridWeb.License.

{{% /alert %}}

###  **Как применить лицензию с диска или потока**

Самый простой способ установить лицензию — поместить файл лицензии в ту же папку, что и dll компонента (входит в состав Aspose.Cells.GridWeb), и указать только имя файла без пути.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Когда вы вызываете метод SetLicense, имя лицензии должно совпадать с именем вашего файла лицензии. Например, вы можете изменить имя файла лицензии на «MyLicense.lic.xml». Затем в своем коде вы должны использовать измененное имя лицензии (т. е. MyLicense.lic.xml) для метода SetLicense.

{{% /alert %}}

Также есть возможность загрузить лицензию из потока.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **Как применить лицензию в качестве встроенного ресурса**

Еще один удобный способ упаковать лицензию вместе с вашим приложением и гарантировать, что она не будет потеряна, — включить ее в качестве встроенного ресурса в одну из сборок, которая вызывает dll компонента (включена в Aspose.Cells.GridDesktop). Чтобы включить файл лицензии в качестве встроенного ресурса, выполните следующие действия:

1.  В Visual Studio .NET включите файл лицензии (.lic) в проект, используя**Добавить существующий элемент** вариант на**Файл** меню.
1. Выберите файл в обозревателе решений и в окне свойств установите для параметра «Действие сборки» значение «Встроенный ресурс».
1. Чтобы получить доступ к лицензии, встроенной в сборку (как внедренный ресурс), не требуется вызывать методы GetExecutingAssembly и GetManifestResourceStream класса System.Reflection.Assembly Microsoft .NET Framework. Вместо этого добавьте файл лицензии в качестве встроенного ресурса в вашу проект и передайте имя файла лицензии в метод SetLicense. Класс License автоматически находит файл лицензии во внедренных ресурсах.

Ознакомьтесь с приведенным ниже примером, чтобы понять этот метод применения лицензии в качестве встроенного ресурса в ваших приложениях.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

##  **Как применить лицензию в Aspose.Cells.GridDesktop для приложения WinForm**

Рекомендуется поместить лицензионный код перед запуском приложения и применить его только один раз. Например, для приложения Windows C# поместите код лицензии в метод Main.

{{< highlight "csharp" >}}

public class Form1 : System.Windows.Forms.Form

{

private Aspose.Cells.GridDesktop.GridDesktop gridDesktop1;

/// <summary>

/// Required designer variable.

/// </summary>

private System.ComponentModel.Container components = null;

public Form1()

{

//

// Required for Windows Form Designer support

//

InitializeComponent();

//

// TODO: Add any constructor code after InitializeComponent call

//

}

/// The main entry point for the application.

/// </summary>

.

.

.

.

[STAThread]

static void Main()

{

Aspose.Cells.GridDesktop.License lic = new Aspose.Cells.GridDesktop.License();

//Use this line if you are using an explicit path for the license file.

lic.SetLicense(@"C:\MyLicense.lic");

//Or use the line below if you are using the license file as an embedded resource.

//lic.SetLicense("MyLicense.lic");

Application.Run(new Form1());

}

private void Form1_Load(object sender, System.EventArgs e)

{

Aspose.Cells.GridDesktop.Worksheet sheet = this.gridDesktop1.Worksheets.Add("MySheet");

sheet.Cells["A1"].SetCellValue("Hello");

gridDesktop1.ActiveSheetIndex = 1;

}

}

{{< /highlight >}}

##  **Примечания по применению лицензии в Aspose.Cells.GridWeb**

Рекомендуется поместить код лицензии в Global.asax.cs вашего веб-приложения (предполагается, что этот файл лицензии находится на диске «d:\»):

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

Загрузка лицензии из потока

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
