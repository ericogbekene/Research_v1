"use client"
import Navbar from "@/components/ui/mainnav";
import Image from "next/image";
import { Button } from "@/components/ui/button";
import { Axis3DIcon } from "lucide-react";
import axios from "axios";
import { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent } from "@/components/ui/card"
import ClientCard from "@/components/ui/clientCard";
import { useEffect } from "react";
import { useState } from "react";

interface Project {
  userId: number
  id: number
  title: string
  completed: boolean
}

/**
  const getProjects = async () => {
  const projects_url = 'https://jsonplaceholder.typicode.com/todos/'
  try {
    const response = await fetch(projects_url)
    return response.json()

  } catch (error) {
    console.log(error)
    return []
  }
}
**/

export default function Home() {
  const [projects, setProjects] = useState<Project[]>([])
  /*const [loading, setIsLoading] = useState<boolean>(true)*/
  const projectsUrl = 'https://jsonplaceholder.typicode.com/todos/'

  useEffect(() => {
    const getResults = async () => {

      try {
        const response = await fetch(projectsUrl)
        const data = await response.json()
        setProjects(data)
      } catch (error) {
        console.error(error)
      } finally {
        //setIsLoading(false)
      }
    };

    getResults();
  }, [])

  return (
    <>
    
    <ClientCard projects={projects} />
    </>
    
  )
}