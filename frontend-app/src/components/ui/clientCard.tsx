"use client"

import { Button } from "./button"
import { Card, CardDescription, CardHeader, CardContent, CardFooter, CardTitle } from "./card"
import Link from "next/link"
import { Project } from "@/app/page"
import { ClientCardProps } from "@/app/page"

export default function ClientCard({ projects}: ClientCardProps) {
    return (
        <div className="client-card">
            <main className="flex min-h-screen bg-slate-300 flex-col items-center justify-between p-24">
                <h1 className="text-2xl mb-4"> Browse Our Collection of Expertly written Academic Papers </h1>
                <div className="">
                    {
                        projects?.map((project ) => {
                            return (
                                <div key={project.id}>
                                    <Card >
                                        <CardHeader>
                                            <CardTitle>{project.title}</CardTitle>
                                            
                                        </CardHeader>

                                        <CardContent>
                                            <div className="flex items-center justify-start gap-2">
                                            <Button asChild>
                                                <Link href="/hire-writer"> View More </Link>

                                            </Button>
                                            <Button asChild>
                                                <Link href="/hire-writer"> Hire Writer </Link>

                                            </Button>
                                            </div>
                                            
                                        </CardContent>
                                        <CardFooter>
                                            <p></p>
                                        </CardFooter>



                                    </Card>
                                </div>

                            )
                        })
                    }
                </div>


            </main>
        </div >
    )
}