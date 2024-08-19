"use client"

import { Button } from "./button"
import { Card, CardDescription, CardHeader, CardContent, CardFooter, CardTitle } from "./card"

export default function ClientCard({ projects }) {
    return (
        <div>
            <main className="flex min-h-screen flex-col items-center justify-between p-24">
                <h1> Browse Our Collection of Expertly written Academic Papers </h1>
                <div className="">
                    {
                        projects?.map((project) => {
                            return (
                                <div className="grid grid-cols-4 gap-8">
                                    <Card key={project.id}>
                                        <CardHeader>
                                            <CardTitle>{project.title}</CardTitle>
                                            <CardDescription>Lorem Ipsum </CardDescription>
                                        </CardHeader>

                                        <CardContent>
                                            <p>Card Content</p>
                                        </CardContent>
                                        <CardFooter>
                                            <p>Card Footer</p>
                                        </CardFooter>



                                    </Card>
                                </div>

                            )
                        })
                    }
                </div>

                <Button> Click Me</Button>
            </main>
        </div >
    )
}