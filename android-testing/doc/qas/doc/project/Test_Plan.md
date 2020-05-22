# Test Plan for Android Testing Suite
May 20th, 2020  
SDET: *Luis Enrique Correa Morán*

## Table of Contents
1. [Project Definition](#10-project-definition)
2. [Scope](#20-scope)
3. [Testing Levels](#30-testing-levels)
4. [Test Strategy](#40-test-strategy)
5. [Exit Criteria](#50-exit-criteria)
6. [Risk Analysis](#60-risk-analysis)
7. [Project Planning](#70-project-planning)

## 1.0 Project Definition
Android Testing Suite is a Software Development that aims to create an in-house testing suite for some of Android's most important modules.
The testing suite is expected to guarantee the correct app behaviour for the Phone, Calculator and Settings apps. It is expected for the framework to be highly optimized, flexible and scalable to accommodate for a variety of different modules (or Apps) in the future.

## 2.0 Scope
The project will cover the following areas for the described three modules of the Android ecosystem.

* Phone App  
    * Ability of performing local calls.  
    * Ability to make international calls.  
    * Ability to reach emergency numbers.  
* Calculator  
    * Correct handling of the sum, division, subtraction and multiplication operations.  
    * Correct handling of complex operations.  
    * Handling of edge cases with arithmetic errors and exceptions.  
    
* WiFi Settings  
    * Ability to perform state changes on the WiFi connectivity for a device.  

### 2.1 Out of Scope
Any interaction of the aforementioned apps with external apps or devices will be left out of the testing scope. All tests must be run in app and on device.  
Also, it is important to mention that the testing suite will only cover the development of the core Android Apps in 
their 'Vanilla' version, what's often described as Pure Android versions of the apps, as OEM personalization layers may introduce screen elements that may be too 
much to generalize and create an optimized framework.

## 3.0 Testing Levels
This project will focus black box testing, evaluating only the outcome of a given process. The testing suite will provide both **system** and **regression** testing to the Android core app development. As the testing framework will provide a comprehensive way of testing the work of all the components of an app, and to guarantee the app's behaviour on every release.  

## 4.0 Test Strategy
The testing developed for this project will consist mainly on System Testing as well as Integration Testing, it is expected from the developers of Android Apps to perform the relevant Unit Testing before pushing new builds for testing.

At the same time, the following roles have been identified to be required for the project.  
| Role           | Responsibilities                                                                                                                                                                                                         |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SDET           | Review test documentation, and verify all of the testing activities performed help towards the testing objectives of the project.                                                                                        |
| Tester         | To execute the tools created for the project, to make software evaluation and reports.                                                                                                                                   |
| Lead Developer | To coordinate all development activities, and organizing all of them so that schedules are met. Review architectural design for the testing tools and prepare all needed environments for the Testing Suite to run over. |
| Developers     | To develop the required tools and processes for testing throughout the project. All of this must be documented.                                                                                                          |

## 5.0 Exit Criteria
For a release to be approved and deployed, the following conditions must be met.  
* The targeted version must pass 97% of the planned test cases.
* All bugs in the released have been identified, analyzed and documented.
* The Project's Lead Developer & Tester have agreed the found bugs do not represent a risk for the platforms overall functionality or credibility.
* All changes have been documented and all reasonable Test Suites have been run to validate the current build.

## 6.0 Risk Analysis

## 7.0 Project Planning

