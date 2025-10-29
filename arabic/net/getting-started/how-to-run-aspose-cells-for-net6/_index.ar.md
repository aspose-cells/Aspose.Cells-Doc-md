---
title: كيفية تشغيل Aspose.Cells for .Net6
type: docs
description: "كيفية تشغيل Aspose.Cells for .Net6."
weight: 138
url: /ar/net/how-to-run-aspose-cells-for-net6/
---

## نظرة عامة

بالنسبة لمنصات .NET6 (أو أحدث) ، يُقارن مع منصات سابقة (.netcore31 أو قبل ذلك) ، الفارق الهام هو حول مكتبة الرسومات. 
في هذا المستند الرسمي [Microsoft Document](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only) ، يشرح للإصدارات .NET6 أو أحدث مكتبة الرسومات "System.Drawing.Common" ستدعم فقط على نظام التشغيل Windows ، ويقدم توصيات لاستبدال مكتبة الرسومات.

بالنسبة لمنتج Apose.Cells، قمنا بإجراء التقييم وقمنا بإكمال ترحيل مكتبة الرسومات. نحن نستخدم SkiaSharp بدلاً من System.Drawing.Common في أنظمة غير ويندوز، كما اقترح في وثائق مايكروسوفت الرسمية. يرجى ملاحظة أن هذا التغيير الحرج سيكون ساري المفعول في Aspose.Cells 22.10.1 أو أحدث لـ .Net6.

بالنسبة لـ .netcore31 أو قبل ذلك ، من أجل التوافق والاستقرار ، نحن نستخدم حاليًا مكتبة الرسومات "System.Drawing.Common". تعتمد الاعتماديات لـ .netcore31 أو قبل ذلك على ما يلي:
- System.Drawing.Common, 5.0.3.
- System.Security.Cryptography.Pkcs، 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

## تشغيل Aspose.Cells لـ .Net6 (أو gerter) على Windows

أولاً يمكنك إنشاء تطبيق .net6 (أو gerter) باستخدام VS2022، ثم يمكنك اختيار خيارات التثبيت التالية:

### التثبيت من خلال Nuget

1. البحث عن Aspose.Cells من NuGet: [Aspose.Cells for .NET حزمة NuGet](https://www.nuget.org/packages/Aspose.Cells/). 
يمكنك أيضًا تثبيت Aspose.Cells من مدير حزم Nuget في VS2022.

2. سيتم تثبيت "SkiaSharp" أو "System.Drawing.Common" تلقائيًا كاعتمادية لـ Aspose.Cells 22.10.1 أو أحدث لمنصات .Net6 (أو gerter)، والتي تعتمد على تكوين "Target OS" في مشروعك.
- اضبط "Target OS" على "Windows" لمشروعك، ستستخدم "System.Drawing.Common" كاعتمادية على نظام Windows الخاص بك لـ .Net6 (أو gerter). في هذا التكوين، يكون ناتج الرسم أقرب إلى .netcore31 أو قبل ذلك.
**![تكوين نظام OS الهدف](TargetOS.png)**
- اضبط "Target OS" على "None" أو خيارات أخرى لمشروعك، ستستخدم "SkiaSharp" كاعتمادية على نظام Windows الخاص بك لـ .Net6 (أو gerter). *يرجى ملاحظة أن الإصدار الذي يستخدم "SkiaSharp" كاعتمادية لا يدعم وظيفة الطباعة على الطابعة.*

### تثبيت من خلال msi أو DLL

1. [قم بتنزيل Aspose.Cells.msi أو DLL](https://releases.aspose.com/cells/net/)

2. قم بفتح دليل التثبيت أو دليل DLL، ثم حدد الخطوة 3 أو 4 أدناه:

3. قم بتحديد مجلد "net6.0-windows"، وأضف Aspose.Cells.dll فيه لتطبيق .net6 الخاص بك. ثم قم بإضافة الحزم التالية يدوياً إلى مشروع .net6 الخاص بك:
- System.Drawing.Common, 6.0.0.
- System.Security.Cryptography.Pkcs، 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

بهذه الطريقة، ستستخدم "System.Drawing.Common" كاعتمادية على نظام Windows الخاص بك لـ .Net6 (أو gerter). في هذا التكوين، يكون ناتج الرسم أقرب إلى .netcore31 أو قبل ذلك.

4. قم بتحديد مجلد "net6.0"، وأضف Aspose.Cells.dll فيه لتطبيق .net6 الخاص بك. ثم قم بإضافة الحزم التالية يدوياً إلى مشروع .net6 الخاص بك:
- SkiaSharp، 3.116.1.
- System.Security.Cryptography.Pkcs، 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

بهذه الطريقة، ستستخدم "SkiaSharp" كاعتمادية على نظام Windows الخاص بك لـ .Net6 (أو gerter). *يرجى ملاحظة أن الإصدار الذي يستخدم "SkiaSharp" كاعتمادية لا يدعم وظيفة الطباعة على الطابعة.*

## تشغيل Aspose.Cells لـ .Net6 (أو gerter) على Linux

يرجى الإشارة إلى طريقة التثبيت على نظام الويندوز، يمكنك فقط تحديد SkiaSharp كتبعية لمكتبة الرسومات على نظام Linux.

ستحتاج إلى القيام بالعمليات الإضافية التالية لضمان استخدام صحيح للSkiaSharp تحت نظام Linux:

1. قم بتشغيل الأمر التالي في نظام Linux الخاص بك:
```
apt-get update && apt-get install -y libfontconfig1
```
أو
```
apk update && apk add fontconfig 
```

2. أضف حزمة NuGet "SkiaSharp.NativeAssets.Linux 3.116.1" إلى مشروعك .net6 (أو gerter).
3. أو يمكنك اختيار إضافة حزم NuGet "SkiaSharp.NativeAssets.Linux.NoDependencies 3.116.1" إلى مشروعك .net6 (أو gerter)، بدلاً من الخطوتين السابقتين.

*يرجى ملاحظة أن إصدار الحزمة المضافة "SkiaSharp.NativeAssets.Linux" أو "SkiaSharp.NativeAssets.Linux.NoDependencies" يجب أن يتوافق مع إصدار "SkiaSharp" المشار إليه بواسطة Aspose.Cells for .NET. الإصدارات الخاصة بـ Aspose.Cells for .NET والإصدارات المرتبطة من "SKiaSharp" موصوفة كالتالي:*

| Aspose.Cells for .NET  |                SkiaSharp                |
| :--------------------: | :-------------------------------------: |
| >= 22.10.1 && <= 22.11 |                 2.88.0                  |
|  >= 22.12 && <= 23.9   |                 2.88.3                  |
|  >= 23.10 && <= 24.12  |                 2.88.6                  |
|        = 25.1.1        |                 3.116.1                 |
|        >=25.1.2        | 2.88.9 (net6.0, net8.0)، 3.116.1 (net9.0) |



### ملف Dockerfile مثالي لأوبونت

1. أضف حزمة NuGet "SkiaSharp.NativeAssets.Linux 3.116.1" إلى مشروعك .net6 (أو gerter).

2. استخدم ملف Dockerfile التالي:
{{< highlight plain >}}
# Ubuntu 20.04
FROM mcr.microsoft.com/dotnet/runtime:6.0-focal AS base
WORKDIR /app

# add "libfontconfig1" package if using "SkiaSharp.NativeAssets.Linux" in your project
# Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apt-get update && apt-get install -y libfontconfig1

# Copy fonts from local to docker
# For example, put a "fonts" folder in your project folder, and put the font files in it,
# then, use the following line:
COPY fonts/ /usr/share/fonts

FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build
WORKDIR /src
COPY ["Ubuntu_Docker.csproj", "."]
RUN dotnet restore "./Ubuntu_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Ubuntu_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ubuntu_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ubuntu_Docker.dll"]
{{< /highlight >}}

### ملف Dockerfile مثالي لألبين

1. أضف حزمة NuGet "SkiaSharp.NativeAssets.Linux 3.116.1" إلى مشروعك .net6 (أو gerter).

2. استخدم ملف Dockerfile التالي:
{{< highlight plain >}}
#Alpine 3.16
FROM mcr.microsoft.com/dotnet/runtime:6.0-alpine3.16 AS base
WORKDIR /app

# add "fontconfig" package if using "SkiaSharp.NativeAssets.Linux" in your project
# Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apk update && apk add fontconfig 

# Copy fonts from local to docker
# For example, put a "fonts" folder in your project folder, and put the font files in it,
# then, use the following line:
COPY fonts/ /usr/share/fonts

FROM mcr.microsoft.com/dotnet/sdk:6.0-alpine3.16 AS build
WORKDIR /src
COPY ["Alpine_Docker.csproj", "."]
RUN dotnet restore "./Alpine_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Alpine_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Alpine_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Alpine_Docker.dll"]
{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
