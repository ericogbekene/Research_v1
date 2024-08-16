"use client"
import { Navbar } from "@/components/ui/mainnav";
import Image from "next/image";
import { Button } from "@/components/ui/button";
import { Axis3DIcon } from "lucide-react";
import axios from "axios";
import { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent } from "@/components/ui/card"
import clientCard from "@/components/ui/clientCard";
import { useEffect } from "react";
import { useState } from "react";

const getProjects = async () => {
  const projects_url = 'https://jsonplaceholder.typicode.com/todos/1'
  try {
    const response = await fetch(projects_url)
    return response.json()

  } catch (error) {
    console.log(error)
    return []
  }
}

export default async function Home() {
  


  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1> Hello from next app</h1>

      {projects.map(project => {
        <Card key={project.id}>
        </Card>
      })}
      <Button> Click Me</Button>
    </main>
  );
}
