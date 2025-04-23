---
title: كيفية تشغيل Aspose.Cells في Docker
type: docs
description: "تشغيل Aspose.Cells في حاوية Docker لنظام Linux، خادم Windows وأي نظام تشغيل آخر."
weight: 139
url: /ar/net/how-to-run-aspose-cells-in-docker/
---

تجعل الخدمات الصغيرة، بالتزامن مع تحتوين الحاويات، من الممكن الجمع بسهولة بين التقنيات. يتيح لك Docker دمج وظائف Aspose.Cells بسهولة في تطبيقك، بغض النظر عن التقنية المستخدمة في مكدس التطوير الخاص بك.

في حال كنت تستهدف الخدمات الصغيرة، أو إذا كانت التقنية الرئيسية في مكدسك ليست .NET أو C++ أو Java، ولكنك بحاجة إلى وظائف Aspose.Cells، أو إذا كنت تستخدم بالفعل Docker في مكدسك، فقد تكون مهتمًا بالاستفادة من Aspose.Cells في حاوية Docker.

## متطلبات قبلية

- يجب تثبيت Docker على نظامك. للحصول على معلومات حول كيفية تثبيت Docker على Windows أو Mac، راجع الروابط في قسم "انظر أيضًا".

- كما لاحظ أن Visual Studio 2019 و .NET Core 3.1 SDK مستخدمان في المثال المقدم أدناه.


## تطبيق Hello World

في هذا المثال، ستقوم بإنشاء تطبيق وحدة تحكم بسيط Hello World الذي يقوم بإنشاء مستند "Hello World!" وحفظه في جميع التنسيقات المدعومة. يمكن بناء التطبيق ثم تشغيله في Docker.

### إنشاء التطبيق لوحدة التحكم

لإنشاء برنامج Hello World، اتبع الخطوات التالية:
1. بمجرد تثبيت Docker، تأكد من استخدام حاويات Linux (الافتراضي). إذا لزم الأمر، حدد الخيار التبديل إلى حاويات Linux من قائمة سطح المكتب لـ Docker.
1. In Visual Studio, create a .NET Core console application.<br>
![todo:image_alt_text](create-a-new-project.png)<br>
1. Install the latest Aspose.Cells version from NuGet. System.Drawing.Common and System.Text.Encoding.CodePages will be installed as a dependency of Aspose.Cells.<br>
![todo:image_alt_text](nuget-aspose-cells.png)<br>
1. نظرًا لأن التطبيق سيتم تشغيله على نظام Linux، يجب تثبيت الأصول الأساسية الأصلية لـ Linux المناسبة. ابدأ باستخدام صورة dotnet core sdk 3.1 الأساسية وقم بتثبيت libgdiplus libc6-dev.
1. When all required dependencies are added, write a simple program that creates a “Hello World!” workbook and saves it in all supported save formats:<br>
**.NET**<br>
{{< highlight csharp >}}
using System;
namespace Aspose.Cells.Docker
{
    class Program
    {
        static void Main(string[] args)
        {
            Workbook workbook = new Workbook();
            workbook.Worksheets[0].Cells[0, 0].PutValue("Hello from Aspose.Cells!!!");
            foreach (SaveFormat sf in Enum.GetValues(typeof(SaveFormat)))
            {
                if (sf != SaveFormat.Unknown)
                {
                    try
                    {
                        // The folder specified will be mounted as a volume when run the application in Docker image.
                        var fileName = string.Format("out{0}", FileFormatUtil.SaveFormatToExtension(sf));
                        workbook.Save(fileName, sf);
                        Console.WriteLine("Saving {0}\t\t[OK]", sf);
                    }
                    catch
                    {
                        Console.WriteLine("Saving {0}\t\t[FAILED]", sf);
                    }
                }
            }
        }
    }
}

{{< /highlight >}}

يرجى ملاحظة أن مجلد "TestOut" محدد كمجلد الإخراج لحفظ مستندات الإخراج. عند تشغيل التطبيق في Docker، سيتم تعليق مجلد على جهاز المضيف بهذا المجلد في الحاوية. سيمكنك بذلك بسهولة عرض الإخراج الذي تم إنشاؤه بواسطة Aspose.Cells في حاوية Docker.

### تكوين ملف Dockerfile

الخطوة التالية هي إنشاء وتكوين ملف Dockerfile.

1. إنشاء ملف Dockerfile ووضعه بجوار ملف الحل التابع لتطبيقك. احتفظ بهذا الاسم كما هو دون امتداد (الافتراضي).
1. في ملف الـDockerfile، حدد:

{{< highlight plain >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
COPY fonts/* /usr/share/fonts/
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]
{{< /highlight >}}

ما تم ذكره أعلاه هو ملف Dockerfile بسيط، ويحتوي على التعليمات التالية:

- الصورة SDK التي سيتم استخدامها. هنا هي صورة .Net Core SDK 3.1. سيقوم Docker بتنزيلها عند تشغيل البناء. يتم تحديد إصدار SDK كوسم.
- تثبيت الخطوط لأن صورة SDK تحتوي على عدد قليل جدًا من الخطوط. تقوم الأمر بنسخ ملفات الخطوط من المضيف المحلي إلى صورة docker. تأكد من وجود "الخطوط" المحلية في دليل نفس الدليل الذي يحتوي على ملف الـDockerfile.
- دليل العمل، الذي يتم تحديده في السطر التالي.
- الأمر لنسخ كل شيء إلى الحاوية، نشر التطبيق وتحديد نقطة الدخول.
- يتم تشغيل الأمر لتثبيت libgdiplus في الحاوية. وهذا مطلوب بواسطة System.Drawing.Common.

### بناء وتشغيل التطبيق في Docker

يمكن الآن بناء التطبيق وتشغيله في Docker. افتح موجه الأوامر المفضلة لديك، غير الدليل إلى المجلد الخاص بالتطبيق (المجلد الذي يوضع فيه ملف الحل وملف الـDockerfile) وقم بتشغيل الأمر التالي.

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

المرة الأولى التي يتم فيها تشغيل هذا الأمر قد يستغرق وقتًا أطول، حيث يحتاج Docker إلى تنزيل الصور المطلوبة. بمجرد الانتهاء من الأمر السابق، قم بتشغيل الأمر التالي:

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

انتبه إلى الوسيطة المرفقة، لأنه كما ذكر سابقًا، يتم تثبيت مجلد في جهاز المضيف في مجلد الحاوية لرؤية نتائج تشغيل التطبيق بسهولة. المسارات في Linux حساسة لحالة الأحرف.

{{% /alert %}}

## الصور التي تدعم Aspose.Cells

- Aspose.Cells for .NET لا تدعم الصورة القياسية EMF و TIFF على Linux.


## أمثلة أخرى

***1. لتشغيل التطبيق في Windows Server 2019***

- Dockerfile

{{< highlight plain >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]
{{< /highlight >}}

- بناء صورة Docker

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- تشغيل صورة Docker

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. لتشغيل التطبيق في نظام Linux***

- كتابة برنامج بسيط يقوم بتعيين مجلد الخطوط وإنشاء سجل عمل "Hello World!" وحفظه

{{< highlight csharp >}}
namespace Aspose.Cells.Docker.Fonts
{
    using System;
    using System.IO;

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Set font folders on linux.
                string[] fonts = { "/Fonts" };
                FontConfigs.SetFontFolders(fonts, true);
                // build workbook
                Workbook workbook = new Workbook();
                MemoryStream memoryStream = new MemoryStream();
                workbook.Worksheets[0].Cells[0, 0].PutValue("Hello from Aspose.Cells!!!");
                Style style = workbook.CreateStyle();
                style.Font.Name = "Arial";
                style.Font.Size = 16;
                workbook.Worksheets[0].Cells[0, 0].SetStyle(style);
                workbook.Save("/TestOut/TestFontsOut.xlsx");
            }
            catch (Exception e)
            {
                Console.WriteLine("Saving outfonts.xlsx\t\t[FAILED],{0}", e.Message);
            }

        }
    }
}

{{< /highlight >}}
- Dockerfile

{{< highlight plain >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.Fonts.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.Fonts.dll"]
{{< /highlight >}}

- بناء صورة Docker

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- تشغيل صورة Docker

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}


## انظر أيضاً

- [تثبيت Docker Desktop على Windows](https://docs.docker.com/docker-for-windows/install/)
- [تثبيت Docker Desktop على Mac](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019, .NET Core 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- خيار [التبديل إلى حاويات Linux](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers)
- معلومات إضافية حول [.NET Core SDK](https://hub.docker.com/_/microsoft-dotnet-sdk)
{{< app/cells/assistant language="csharp" >}}
