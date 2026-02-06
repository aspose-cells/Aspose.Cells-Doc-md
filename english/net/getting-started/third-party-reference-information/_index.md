---
title: Aspose.Cells Third‐Party Reference Information
description: Detailed guide on how Aspose.Cells references third‐party libraries across .NET versions (net6, net8, net9, net10) on Windows and Linux, including version differences, upgrade impact, and how to inspect referenced assemblies programmatically.
keywords: Aspose.Cells, .NET6, .NET8, .NET9, .NET10, Windows, Linux, third‐party libraries, SkiaSharp, System.Drawing.Common, BouncyCastle, System.Security.Cryptography.Pkcs, System.Text.Encoding.CodePages, reference evolution
type: docs
weight: 140
url: /net/third-party-reference-information/
---

{{% alert color="primary" %}}

This article explains the third‐party assemblies that Aspose.Cells depends on for each supported .NET target framework and operating system. Understanding these dependencies helps you **size your deployment**, **resolve runtime issues**, and **plan upgrades** effectively.

{{% /alert %}}

## **Introduction**

Aspose.Cells for .NET is a multi‐target library. Depending on the **target framework** (net6, net8, net9, net10) and the **runtime OS** (Windows vs. Linux) it pulls different NuGet packages.  
The table‐driven overview below shows:

* Which third‐party packages are referenced for each combination.  
* How those references evolve when you move from one Aspose.Cells version to the next.  
* What changes you should expect when upgrading between major Aspose.Cells releases.

The article also includes a **runnable C# snippet** that lists the actual referenced assemblies of the Aspose.Cells binary at runtime – useful for verifying the exact versions that are loaded in your application.

---

## **Reference Libraries on Windows**

| .NET Target | Aspose.Cells Version | System.Drawing.Common | System.Security.Cryptography.Pkcs | System.Text.Encoding.CodePages | SkiaSharp | BouncyCastle |
|-------------|----------------------|-----------------------|-----------------------------------|--------------------------------|-----------|--------------|
| net6        | **21.12** – 22.6     | 4.7.0                 | –                                 | 4.7.0                          | –         | 1.9.0 |
| net6        | 22.7  – 22.12        | 4.7.0                 | **6.0.1**                         | 4.7.0                          | –         | 1.9.0 |
| net6        | 23.1  – 23.6         | **6.0.0**             | 6.0.1                             | 4.7.0                          | –         | 1.9.0 |
| net6        | 23.7  – 24.11        | 6.0.0                 | **6.0.3**                         | 4.7.0                          | –         | 1.9.0 |
| net6        | 24.12 - 25.9         | 6.0.0                 | **6.0.5**                         | 4.7.0                          | –         | 1.9.0 |
| net6        | 25.10 - 26.X         | 6.0.0                 | 6.0.5                             | 4.7.0                          | –         | **2.6.2** |
| net8        | **24.1** – 24.11     | 6.0.0                 | 6.0.3                             | 4.7.0                          | –         | 1.9.0 |
| net8        | 24.12 - 25.9         | 6.0.0                 | **8.0.1**                         | 4.7.0                          | –         | 1.9.0 |
| net8        | 25.10 - 26.X         | 6.0.0                 | 8.0.1                             | 4.7.0                          | –         | **2.6.2** |
| net9        | **25.1** – 25.9      | 6.0.0                 | 9.0.0                             | 4.7.0                          | –         | 1.9.0 |
| net9        | 25.10 – 26.X         | 6.0.0                 | 9.0.0                             | 4.7.0                          | –         | **2.6.2** |
| net10       | **25.12** - 26.X     | 6.0.0                 | 9.0.0                             | -                              | –         | 2.6.2 |

> **Note** – Starting with Aspose.Cells 25.12(targeting .NET 10) the library no longer requires `System.Text.Encoding.CodePages` on Windows.

---

## **Reference Libraries on Linux**

| .NET Target | Aspose.Cells Version |     SkiaSharp     | System.Security.Cryptography.Pkcs | System.Text.Encoding.CodePages | BouncyCastle |
|-------------|----------------------|-------------------|-----------------------------------|--------------------------------|--------------|
| net6        | **22.10.1** – 22.11  | 2.88.0            | 6.0.1                             | 4.7.0                          | 1.9.0 |
| net6        | 22.12 - 23.6         | **2.88.3**        | 6.0.1                             | 4.7.0                          | 1.9.0 |
| net6        | 23.7 - 23.9          | 2.88.3            | **6.0.3**                         | 4.7.0                          | 1.9.0 |
| net6        | 23.10 - 24.11        | **2.88.6**        | 6.0.3                             | 4.7.0                          | 1.9.0 |
| net6        | 24.12                | 2.88.6            | **6.0.5**                         | 4.7.0                          | 1.9.0 |
| net6        | 25.2 - 25.9          | **2.88.9**        | 6.0.5                             | 4.7.0                          | 1.9.0 |
| net6        | 25.10 - 26.X         | 2.88.9            | 6.0.5                             | 4.7.0                          | **2.6.2** |
| net8        | **24.1** - 24.11     | 2.88.6            | 6.0.3                             | 4.7.0                          | 1.9.0 |
| net8        | 24.12                | 2.88.6            | **8.0.1**                         | 4.7.0                          | 1.9.0 |
| net8        | 25.2 - 25.9          | **2.88.9**        | 8.0.1                             | 4.7.0                          | 1.9.0 |
| net8        | 25.10 - 26.X         | 2.88.9            | 8.0.1                             | 4.7.0                          | **2.6.2** |
| net9        | **25.1** – 25.9      | 3.116.1           | 9.0.0                             | 4.7.0                          | 1.9.0 |
| net9        | 25.10 - 26.X         | 3.116.1           | 9.0.0                             | 4.7.0                          | **2.6.2** |
| net10       | **25.12** - 26.X     | 3.116.1           | 9.0.0                             | -                              | 2.6.2 |

{{% alert color="primary" %}}

*On Linux the rendering engine is SkiaSharp; therefore the version of **SkiaSharp** changes more frequently than on Windows.*  
When you upgrade Aspose.Cells for .NET 6 from **25.1 → 25.2** you will see SkiaSharp jump from **2.88.6** to **2.88.9**. For .NET 9 the dependency moves to **SkiaSharp 3.116.1**.

{{% /alert %}}

---

## **Programmatically Inspecting Referenced Assemblies**

You can verify the exact versions that your application loads at runtime by using reflection. The following **complete, runnable C# example** enumerates all referenced assemblies of the Aspose.Cells core assembly and prints their names and versions.

```csharp
// ------------------------------------------------------------
// Aspose.Cells Reference Inspection Example
// ------------------------------------------------------------
// This console application loads the Aspose.Cells assembly
// and prints all its referenced third‐party libraries.
// ------------------------------------------------------------

using System;
using System.IO;
using System.Linq;
using System.Reflection;
using Aspose.Cells;

namespace AsposeCellsReferenceDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // -----------------------------------------------------------------
            // Ensure the Aspose.Cells NuGet package is referenced in the project.
            // The assembly is located via the type Aspose.Cells.Workbook.
            // -----------------------------------------------------------------
            Assembly cellsAssembly = typeof(Workbook).Assembly;

            Console.WriteLine("Aspose.Cells Assembly:");
            Console.WriteLine($"  Full Name : {cellsAssembly.FullName}");
            Console.WriteLine($"  Location  : {cellsAssembly.Location}");
            Console.WriteLine();

            // Get all referenced assemblies (direct references only)
            AssemblyName[] referenced = cellsAssembly.GetReferencedAssemblies();

            // Sort for readability
            var ordered = referenced.OrderBy(a => a.Name).ToArray();

            Console.WriteLine("Referenced Third‐Party Assemblies:");
            Console.WriteLine("----------------------------------------------------------");
            Console.WriteLine("{0,-35} {1,10}", "Assembly", "Version");
            Console.WriteLine("----------------------------------------------------------");

            foreach (var asm in ordered)
            {
                Console.WriteLine("{0,-35} {1,10}", asm.Name, asm.Version);
            }

            // -----------------------------------------------------------------
            // OPTIONAL: Filter for specific libraries we are interested in.
            // -----------------------------------------------------------------
            string[] targetLibs = new[]
            {
                "System.Drawing.Common",
                "System.Security.Cryptography.Pkcs",
                "System.Text.Encoding.CodePages",
                "SkiaSharp"
            };

            Console.WriteLine();
            Console.WriteLine("Filtered Subset (Target Libraries):");
            Console.WriteLine("----------------------------------------------------------");
            foreach (string lib in targetLibs)
            {
                var match = ordered.FirstOrDefault(a => a.Name.Equals(lib, StringComparison.OrdinalIgnoreCase));
                if (match != null)
                {
                    Console.WriteLine($"{match.Name,-35} {match.Version}");
                }
                else
                {
                    Console.WriteLine($"{lib,-35} <not referenced>");
                }
            }

            // Keep console window open when debugging.
            Console.WriteLine();
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }
    }
}
```

**How to run the sample**

1. Create a new .NET 6/8/9/10 console project (`dotnet new console`).
2. Add the Aspose.Cells NuGet package (`dotnet add package Aspose.Cells`).
3. Replace the auto‐generated `Program.cs` with the code above.
4. Build and run (`dotnet run`).  
   The output will list the exact versions of the third‐party libraries that the current Aspose.Cells build depends on on your OS.

---

{{% alert color="primary" %}}

**Quick checklist before upgrading**  

* Verify the SkiaSharp native libraries are present in your Linux Docker image.  
* Remove any explicit binding redirects for `System.Security.Cryptography.Pkcs` when targeting .NET 10.  
* Re‐run the **Reference Inspection** sample after upgrade to confirm that the expected versions are loaded.

{{% /alert %}}

--- 

*For a full list of all Aspose.Cells NuGet versions and their dependency trees, visit the official NuGet package page: https://www.nuget.org/packages/Aspose.Cells/*
