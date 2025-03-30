cmake_minimum_required(VERSION 3.30)
project(BalanceTree)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
include_directories(x64)
include_directories(x64/Debug)

add_executable(BalanceTree
    x64/Debug/BalanceTree.pch
    AVLTree.cpp
    AVLTree.h
    AVLTree2.cpp
    AVLTree2.h
    BSTree.cpp
    BSTree.h
    BSTree2.cpp
    BSTree2.h
    RBTree.cpp
    RBTree.h
    RBTree2.cpp
    RBTree2.h
    RBTree3.cpp
    RBTree3.h
    stdafx.cpp
    stdafx.h
    StlSet.cpp
    StlSet.h
    targetver.h
    TestTree.cpp
    Tree.cpp
    Tree.h
    TreeNode.cpp
    TreeNode.h)
